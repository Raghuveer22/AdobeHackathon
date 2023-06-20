import os
import json
import shutil
import logging
import zipfile
from logging_utils import setup_logging
from pdf_operations import create_execution_context, extract_pdf,get_auto_tag_pdf
from zip_data_processing import extract_and_process

BASEPATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def process_pdf(source_file_path, execution_context):
    result_file_path = extract_pdf(source_file_path=source_file_path, execution_context=execution_context)
    if result_file_path is not None:
        return extract_and_process(zip_file_path=result_file_path)
    else:
        return None


def process_files(source_folder, execution_context):
    master_data = {}
    failed_files = []
    for source_file in os.listdir(source_folder):
        source_file_path = os.path.join(source_folder, source_file)
        if source_file.endswith(".pdf"):
            data = process_pdf(source_file_path, execution_context)
            if data is not None:
                master_data[source_file] = data   
            else:
                failed_files.append(source_file)
        else:
            logging.error(f"Error processing file '{source_file}'. File extension not supported.")

    return master_data, failed_files


def update_master_data_with_failed_files(master_data,source_folder,failed_files, execution_context):
    missed_data = {}
    for failed_file in failed_files:
        source_file_path = os.path.join(source_folder, failed_file)
        tagged_pdf_path=get_auto_tag_pdf(execution_context=execution_context,source_file_path=source_file_path)
        if tagged_pdf_path is not None:
            result_file_path = extract_pdf(source_file_path=tagged_pdf_path, execution_context=execution_context)
            if result_file_path is not None:
                data = extract_and_process(zip_file_path=result_file_path)
                if data is not None:
                    missed_data[failed_file] = data
    master_data.update(missed_data)
    return master_data


def write_master_data_to_json(master_data, file_path):
    with open(file_path, 'w') as file:
        json.dump(master_data, file)



def write_failed_files(failed_files, file_path):
    with open(file_path, 'w') as file:
        for failed_file in failed_files:
            file.write(failed_file + '\n')
    
def save_json(file,source_folder,save_folder,execution_context):
    source_file_path=os.path.join(source_folder,file)
    tagged_pdf_path=get_auto_tag_pdf(execution_context=execution_context,source_file_path=source_file_path)
    if tagged_pdf_path is not None:
        result_file_path = extract_pdf(source_file_path=tagged_pdf_path, execution_context=execution_context)
    file_name,_=file.split(".")
    new_file_name=file_name+".json"
    if result_file_path is not None:
        with zipfile.ZipFile(result_file_path, 'r') as zip_file:
            extracted_file_name = zip_file.namelist()[0]  # Get the name of the first extracted file
            extracted_file_path = os.path.join(save_folder, extracted_file_name)
            zip_file.extractall(path=save_folder)
        new_file_path = os.path.join(save_folder, new_file_name)
        os.rename(extracted_file_path, new_file_path)  # Rename the extracted file to the desired name    
        return 200
    else:
        return 404

MAX_RETRY_LIMIT = 3
json_file="invoice.json"
failed_file="failed_files.txt"
def main():
    setup_logging()
    execution_context = create_execution_context()
    source_folder = os.path.join(BASEPATH, 'Master', 'InvoicesData', 'TestDataSet')
    print(source_folder)
    master_data, failed_files = process_files(source_folder, execution_context)
    write_master_data_to_json(master_data, json_file)
    retry_count = 0
    while failed_files and retry_count < MAX_RETRY_LIMIT:
        master_data = update_master_data_with_failed_files(master_data, source_folder, failed_files, execution_context)
        write_master_data_to_json(master_data,json_file)
        failed_files = [file for file in failed_files if file not in master_data]
        retry_count += 1
        
    if failed_files:
        write_failed_files(failed_files, failed_file)
        logging.error("Failed to process some files after reaching the maximum retry limit. The list of failed files has been saved to 'failed_files.txt'.")
    logging.info("Processing completed successfully.")
    
if __name__=="__main__":
    main()
