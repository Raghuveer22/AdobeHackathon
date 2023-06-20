import zipfile
import json
import os
import tempfile
import logging
import re
def extract_and_process(zip_file_path):
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            for file_info in zip_ref.infolist():
                if file_info.filename == 'structuredData.json':
                    with zip_ref.open(file_info) as source, open(temp_file.name, 'wb') as dest:
                        dest.write(source.read())
                    data = get_data(temp_file.name,exeception=0)
    os.unlink(temp_file.name)  # Remove the temporary file
    return data

def extract_elements_from_json(json_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        json_data = json.load(json_file)
        elements = json_data['elements']
        return elements

def get_data(json_file_path,exeception):
    data = []
    elements = extract_elements_from_json(json_file_path)
    for  element in elements:
        if "Text" in element:
            data.append(str(element["Text"].encode().decode('unicode-escape').strip()))
    substring = "Tax %"
    pattern = re.compile(re.escape(substring))  
    if exeception==0:
        found = False
        for element in data:
            if re.search(pattern, element):
                found = True
                break
        if found:
            return data
        else:
            logging.exception("Tax %\ is no present in the text")
            return None
    else:
        return data