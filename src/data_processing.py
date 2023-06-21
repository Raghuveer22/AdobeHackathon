import re
import json
import csv
import os
def regex_match(pattern, string, group=0):
    """
    Helper function to perform regular expression matching.

    Args:
        pattern (str): The regular expression pattern.
        string (str): The string to match against.
        group (int): The group number to return (default: 0).

    Returns:
        str: The matched group or an empty string if no match is found.
    """
    match = re.search(pattern, string)
    if match:
        return match.group(group)
    else:
        return ""


def remove_words(words, string):
    """
    Remove specified words from a string and clean up extra spaces and values with dollar.

    Args:
        words (list): The list of words to remove.
        string (str): The string to modify.

    Returns:
        str: The modified string with words removed and cleaned up.
    """
    for word in words:
        string = string.replace(word, "")
    string = re.sub('\$\d+(\.\d+)?', '', string)
    string = re.sub('\s+', ' ', string)
    string = string.replace('$', '')
    return string.strip()


def extract_and_remove_pattern(pattern, string):
    """
    Extracts a word based on a pattern from a string and removes it.

    Args:
        pattern (str): The regular expression pattern to match and extract.
        string (str): The string to modify.

    Returns:
        tuple: The extracted word and the modified string.
    """
    word = regex_match(pattern, string)
    return word, remove_words([word], string)


def remove_numbers_greater_than_100(text):
    """
    Remove numbers greater than 100 from the text.

    Args:
        text (str): The text to modify.

    Returns:
        str: The modified text with numbers greater than 100 removed.
    """
    words = text.split()
    result = []

    for word in words:
        if word.isdigit() and int(word) <= 100:
            result.append(word)
    if not result:
        return ""
    return ' '.join(result)


def write_data_to_csv(filename, data):
    """
    Write data to a CSV file.

    Args:
        filename (str): The name of the CSV file to write.
        data (list): The list of dictionaries containing the data.

    Returns:
        None
    """
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


def extract_business_details(value_list):
    """
    Extract business details from the value list.

    Args:
        value_list (list): The list of values.

    Returns:
        tuple: The extracted business details.
    """
    bussiness_name = value_list[0]
    next_index = value_list[1:].index(bussiness_name)
    bussiness_description = value_list[next_index + 2]
    bussiness_address_list = value_list[1:next_index + 1]
    temp = " ".join(bussiness_address_list)
    bussiness_zip_code = regex_match(r'\b\d{5}\b', temp)
    bussiness_address = temp.split(f"{bussiness_zip_code}")[0].strip()
    bussiness_address_list = bussiness_address.split(', ')
    bussiness_street_address = bussiness_address_list[0]
    bussiness_city = bussiness_address_list[1]
    bussiness_country_list = bussiness_address_list[2:]
    bussiness_country = ", ".join(bussiness_country_list)
    invoice_details = temp.split(f"{bussiness_zip_code}")[1].strip()
    issue_date = regex_match(r'\b(\d{2}-\d{2}-\d{4})\b', temp)
    invoice_details = invoice_details.split(f"{issue_date}")[0].strip()
    invoice_number = regex_match(r'(\w+)\sIssue date', invoice_details, group=1)

    return (
        bussiness_city,
        bussiness_country,
        bussiness_description,
        bussiness_name,
        bussiness_street_address,
        bussiness_zip_code,
        issue_date,
        invoice_number,
        next_index
    )


def extract_customer_details(value_list, next_index, item_index):
    """
    Extract customer details from the value list.

    Args:
        value_list (list): The list of values.
        next_index (int): The index of the next value.
        item_index (int): The index of the "ITEM" value.

    Returns:
        tuple: The extracted customer details.
    """
    customer_address_list = value_list[next_index + 4:item_index]
    customer_address = " ".join(customer_address_list)
    due_date, customer_address = extract_and_remove_pattern(r'\b(\d{2}-\d{2}-\d{4})\b', customer_address)
    customer_email, customer_address = extract_and_remove_pattern(r'\b\w+(?:\.\w+)*@\w+(?:\.\w+)?\b', customer_address)
    phone_number, customer_address = extract_and_remove_pattern(r"\d{3}-\d{3}-\d{4}", customer_address)
    customer_address_line1, customer_address = extract_and_remove_pattern(r"\b\d+\b\s+[A-Z][a-zA-Z']+(\s+[A-Z][a-zA-Z']+)?", customer_address)
    words_to_remove = ["DETAILS", "PAYMENT", "Due date:"]
    customer_address = remove_words(words=words_to_remove, string=customer_address)
    customer_name = ' '.join(customer_address.split()[:2])
    words_to_remove = [customer_name]
    customer_address = remove_words(words=words_to_remove, string=customer_address)
    customer_address_list = customer_address.split(" ")
    customer_address_line2_words = []
    for x in customer_address_list:
        if x[0].isupper() and x != "Lorem":
            customer_address_line2_words.append(x)
    customer_address_line2 = " ".join(customer_address_line2_words)
    words_to_remove = [customer_address_line2]
    customer_address = remove_words(words=words_to_remove, string=customer_address)
    invoice_description_list = customer_address.split(" ")
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.com\b'
    match = re.match(pattern, customer_email)
    if not match:
        for index, x in enumerate(invoice_description_list):
            if re.match(pattern, customer_email + x):
                customer_email = customer_email + x
                del invoice_description_list[index]
                break
    invoice_description = " ".join(invoice_description_list)

    return (
        customer_address_line1,
        customer_address_line2,
        customer_email,
        customer_name,
        phone_number,
        invoice_description,
        due_date
    )


def extract_invoice_items(value_list, item_index):
    """
    Extract invoice items from the value list.

    Args:
        value_list (list): The list of values.
        item_index (int): The index of the "ITEM" value.

    Returns:
        tuple: The extracted invoice items and the updated item index.
    """
    products = []
    item_index += 4
    quantity_index = item_index + 1
    rate_index = item_index + 2

    while rate_index < len(value_list):
        if value_list[item_index].find("Subtotal") != -1:
            break
        product = {"item": value_list[item_index], "qty": value_list[quantity_index], "rate": value_list[rate_index]}
        products.append(product)
        item_index += 4
        quantity_index = item_index + 1
        rate_index = item_index + 2

    return products, item_index


def extract_invoice_tax(value_list, item_index):
    """
    Extract invoice tax from the value list.

    Args:
        value_list (list): The list of values.
        item_index (int): The index of the "ITEM" value.

    Returns:
        str: The extracted invoice tax.
    """
    tax_text = " ".join(value_list[item_index:])
    words_to_remove = ["Tax %", "Total", "Due"]
    tax_text = remove_words(words=words_to_remove, string=tax_text)
    tax_text = remove_numbers_greater_than_100(tax_text)

    return tax_text


def extract_data_from_json(filename):
    """
    Extract data from the JSON file.

    Args:
        filename (str): The name of the JSON file.

    Returns:
        list: The extracted data.
    """
    data = []

    with open(filename) as file:
        master_data = json.load(file)

    for i in master_data.keys():
        value_list = master_data[i]
        business_city, business_country, business_description, business_name, business_street_address, business_zip_code, issue_date, invoice_number, next_index = extract_business_details(value_list)
        item_index = value_list.index("ITEM")
        customer_address_line1, customer_address_line2, customer_email, customer_name, phone_number, invoice_description, due_date = extract_customer_details(value_list, next_index, item_index)
        products, item_index = extract_invoice_items(value_list, item_index)
        tax_text = extract_invoice_tax(value_list, item_index)

        for product in products:
            data.append({
                'Bussiness__City': business_city,
                'Bussiness__Country': business_country,
                'Bussiness__Description': business_description,
                'Bussiness__Name': business_name,
                'Bussiness__StreetAddress': business_street_address,
                'Bussiness__Zipcode': business_zip_code,
                'Customer__Address__line1': customer_address_line1,
                'Customer__Address__line2': customer_address_line2,
                'Customer__Email': customer_email,
                'Customer__Name': customer_name,
                'Customer__PhoneNumber': phone_number,
                'Invoice__BillDetails__Name': product["item"],
                'Invoice__BillDetails__Quantity': product["qty"],
                'Invoice__BillDetails__Rate': product["rate"],
                'Invoice__Description': invoice_description,
                'Invoice__DueDate': due_date,
                'Invoice__IssueDate': issue_date,
                'Invoice__Number': invoice_number,
                'Invoice__Tax': tax_text
            })

    return data
# file names and constants used in this file
BASEPATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
json_filename = os.path.join(BASEPATH,"output","invoice.json")
exception_filename = os.path.join(BASEPATH,"output","exception.json")

def main():
    """
    The main function of the program.
    """
    data = extract_data_from_json(json_filename)
    exception_data = extract_data_from_json(exception_filename)
    data = data + exception_data
    write_data_to_csv('output.csv', data)


if __name__ == "__main__":
    main()
