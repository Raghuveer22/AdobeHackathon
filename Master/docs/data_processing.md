Documentation for the provided code:

Title: Invoice Extraction and writing to a csv file

Introduction:
The code provided is a Python script that extracts data from a JSON file containing invoice information. It performs various data extraction and manipulation tasks to convert the extracted data into a structured format and then writes it to a CSV file. The script utilizes regular expressions and string manipulation techniques to extract specific information from the JSON data.

Functions and Usage:

1. `regex_match(pattern, string, group=0)`:
   - Description: This function performs a regular expression matching operation on a given string using the provided pattern.
   - Parameters:
     - `pattern`: The regular expression pattern to match.
     - `string`: The input string to match against the pattern.
     - `group` (optional): The capturing group index to return. Defaults to 0, which returns the entire match.
   - Returns: The matched substring or an empty string if no match is found.

2. `remove_words(words, string)`:
   - Description: This function removes specified words from a given string, cleans up extra spaces, and removes values in the format of a dollar like example "$","$234"
   - Parameters:
     - `words`: A list of words to remove from the string.
     - `string`: The input string to process.
   - Returns: The processed string with the specified words removed, extra spaces cleaned, and dollar values removed.

3. `remove_numbers_greater_than_100(text)`:
   - Description: This function removes numbers greater than 100 from the input text, specifically targeting values in the format of a percentage (e.g., "Tax%").
   - Parameters:
     - `text`: The input text to process.
   - Returns: The processed text with numbers greater than 100 removed.

4. `write_data_to_csv(filename, data)`:
   - Description: This function writes the provided data to a CSV file.
   - Parameters:
     - `filename`: The name of the CSV file to create or overwrite.
     - `data`: A list of dictionaries, where each dictionary represents a row of data to be written to the CSV file.
   - Returns: None

5. `extract_business_details(value_list)`:
   - Description: This function extracts business details from the given value list.
   - Parameters:
     - `value_list`: A list of values extracted from the JSON data.
   - Returns: A tuple containing the extracted business details, including city, country, description, name, street address, and ZIP code.

6. `extract_invoice_details(value_list, next_index)`:
   - Description: This function extracts invoice details from the given value list.
   - Parameters:
     - `value_list`: A list of values extracted from the JSON data.
     - `next_index`: The index of the next occurrence of the business name in the value list.
   - Returns: A tuple containing the extracted issue date and invoice number.

7. `extract_and_remove_pattern(pattern, string)`:
   - Description: This function extracts a substring matching the given pattern from the string and removes it from the string.
   - Parameters:
     - `pattern`: The regular expression pattern to match.
     - `string`: The input string to process.
   - Returns: A tuple containing the extracted word and the processed string with the word removed.

8. `extract_customer_details(value_list, next_index, item_index)`:
   - Description: This function extracts customer details from the given value list.
   - Parameters:
     - `value_list`: A list of values extracted from the JSON data.
     - `next_index`: The index of the next occurrence of the business name in the value list.
     - `item_index`: The index of the "ITEM" keyword in the value list.
   -

 Returns: A tuple containing the extracted customer address line 1, address line 2, email, name, phone number, invoice description, and due date.

9. `extract_invoice_items(value_list, item_index)`:
   - Description: This function extracts invoice items from the given value list.
   - Parameters:
     - `value_list`: A list of values extracted from the JSON data.
     - `item_index`: The index of the "ITEM" keyword in the value list.
   - Returns: A list of dictionaries representing the extracted invoice items, including the item name, quantity, and rate.

10. `extract_invoice_tax(value_list, item_index)`:
    - Description: This function extracts invoice tax information from the given value list.
    - Parameters:
      - `value_list`: A list of values extracted from the JSON data.
      - `item_index`: The index of the "ITEM" keyword in the value list.
    - Returns: The extracted invoice tax information.

11. `extract_data_from_json(filename)`:
    - Description: This function extracts data from a JSON file, performs various extraction operations using the previously defined functions, and returns the extracted data as a list of dictionaries.
    - Parameters:
      - `filename`: The name of the JSON file to read.
    - Returns: A list of dictionaries representing the extracted data.

12. `main()`:
    - Description: The main entry point of the script. It specifies the JSON filename, extracts the data using `extract_data_from_json()`, and writes the extracted data to a CSV file using `write_data_to_csv()`.

Usage:
To use the code:
1. Ensure that the required Python libraries (re, json, csv) are installed.
2. Place the code in a Python script file (e.g., `invoice_extraction.py`).
3. Provide the path to the JSON file containing the invoice data by modifying the `json_filename` variable in the `main()` function.
4. Run the script, which will extract the data from the JSON file, perform the necessary operations, and generate a CSV file named `output.csv` containing the structured data.

Note:
Please ensure that the input JSON file follows the expected structure and contains the necessary information for the extraction functions to work correctly.