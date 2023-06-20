import re
import json
import csv


def regex_match(pattern, string, group=0):
    # Helper function to perform regular expression matching
    match = re.search(pattern, string)
    if match:
        return match.group(group)
    else:
        return ""


def remove_words(words, string):
    # Remove specified words from a string and clean up extra spaces
    for word in words:
        string = string.replace(word, "")
    string = re.sub('\$\d+(\.\d+)?', '', string)
    string = re.sub('\s+', ' ', string)
    string = string.replace('$', '')
    return string.strip()


def remove_numbers_greater_than_100(text):
    # Remove numbers greater than 100 from the text
    words = text.split()
    result = []
    
    for word in words:
        if not word.isdigit() or int(word) <= 100:
            result.append(word)
    
    return ' '.join(result)


def write_data_to_csv(filename, data):
    # Write data to a CSV file
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


def extract_business_details(value_list):
    # Extract business details from the value list
    bussiness_name = value_list[0]
    next_index = value_list[1:].index(bussiness_name)
    bussiness_description = value_list[next_index + 2]
    bussiness_address_list = value_list[1:next_index + 1]
    bussiness_address_full = " ".join(bussiness_address_list)
    bussiness_zip_code = regex_match(r'\b\d{5}\b', bussiness_address_full)
    bussiness_address = bussiness_address_full.split(f"{bussiness_zip_code}")[0].strip()
    bussiness_address_list = bussiness_address.split(', ')
    bussiness_street_address = bussiness_address_list[0]
    bussiness_city = bussiness_address_list[1]
    bussiness_country_list = bussiness_address_list[2:]
    bussiness_country = ", ".join(bussiness_country_list)
    
    return bussiness_city, bussiness_country, bussiness_description, bussiness_name, bussiness_street_address, bussiness_zip_code


def extract_invoice_details(value_list, next_index):
    # Extract invoice details from the value list
    issue_date = regex_match(r'\b(\d{2}-\d{2}-\d{4})\b', value_list[next_index])
    invoice_details = value_list[next_index].split(f"{issue_date}")[1].strip()
    invoice_number = regex_match(r'(\w+)\sIssue date', invoice_details, 1)
    
    return issue_date, invoice_number
def extract_and_remove_pattern(pattern, string):
   word= regex_match(pattern,string)
   return  word,remove_words([word],string)
def extract_customer_details(value_list, next_index, item_index):
    # Extract customer details from the value list
    customer_address_list = value_list[next_index + 4:item_index]
    customer_address = " ".join(customer_address_list)
    due_date,customer_address = extract_and_remove_pattern(r'\b(\d{2}-\d{2}-\d{4})\b', customer_address)
    customer_email,customer_address = extract_and_remove_pattern(r'\b\w+(?:\.\w+)*@\w+(?:\.\w+)?\b', customer_address)
    phone_number,customer_address = extract_and_remove_pattern(r"\d{3}-\d{3}-\d{4}", customer_address)
    customer_address_line1,customer_address = extract_and_remove_pattern(r"\b\d+\b\s+[A-Z][a-zA-Z']+(\s+[A-Z][a-zA-Z']+)?", customer_address)
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
    
    return customer_address_line1, customer_address_line2, customer_email, customer_name, phone_number, invoice_description, due_date


def extract_invoice_items(value_list, item_index):
    # Extract invoice items from the value list
    products = []
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

    return products


def extract_invoice_tax(value_list, item_index):
    # Extract invoice tax from the value list
    tax_text = " ".join(value_list[item_index + 1:])
    words_to_remove = ["Tax %", "Total", "Due"]
    tax_text = remove_words(words=words_to_remove, string=tax_text)
    tax_text = remove_numbers_greater_than_100(tax_text)
    
    return tax_text


def extract_data_from_json(filename):
    # Extract data from the JSON file
    data = []
    
    with open(filename) as file:
        master_data = json.load(file)
    
    for i in master_data.keys():
        value_list = master_data[i]
        business_city, business_country, business_description, business_name, business_street_address, business_zip_code = extract_business_details(value_list)
        next_index = value_list[1:].index(business_name)
        issue_date, invoice_number = extract_invoice_details(value_list, next_index)
        item_index = value_list.index("ITEM")
        customer_address_line1, customer_address_line2, customer_email, customer_name, phone_number, invoice_description, due_date = extract_customer_details(value_list, next_index, item_index)
        products = extract_invoice_items(value_list, item_index)
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


def main():
    json_filename = 'invoice.json'
    data = extract_data_from_json(json_filename)
    write_data_to_csv('output.csv', data)


if __name__ == "__main__":
    main()