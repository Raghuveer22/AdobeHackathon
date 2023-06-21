import os
import json
import logging
from logging_utils import setup_logging
from pdf_operations import create_execution_context
from file_extraction import (
    update_master_data_with_failed_files,
    write_master_data_to_json,
    write_failed_files,
    save_json
)

# constants used in the code
BASEPATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
json_file = os.path.join(BASEPATH,"output","invoice.json")# Path to the JSON file storing master data
failed_file = os.path.join(BASEPATH,"output","failed_files.txt") # Path to the text file storing failed file names
MAX_RETRY_LIMIT = 3  # Maximum number of retry attempts for failed files


def main():
    setup_logging()
    source_folder = os.path.join(BASEPATH, 'InvoicesData', 'TestDataSet')
    execution_context = create_execution_context()

    # Load master data from JSON file
    with open(json_file, 'r') as file:
        master_data = json.load(file)

    # Load failed file names from text file
    failed_files = []
    with open(fails_file, 'r') as file:
        for line in file:
            source_file_path = line.strip()
            failed_files.append(source_file_path)

    retry_count = 0
    while failed_files and retry_count < MAX_RETRY_LIMIT:
        master_data = update_master_data_with_failed_files(master_data, source_folder, failed_files, execution_context)
        write_master_data_to_json(master_data, json_file)
        failed_files = [file for file in failed_files if file not in master_data]
        retry_count += 1

    fail_folder = os.path.join(BASEPATH, 'Failed')
    if failed_files:
        logging.error("Failed to process some files after reaching the maximum retry limit")
        for failed_file in failed_files:
            val = save_json(failed_file, source_folder=source_folder, save_folder=fail_folder, execution_context=execution_context)
            if val == 200:
                failed_files.remove(failed_file)
    if failed_files:
        write_failed_files(failed_files, failed_file)
    logging.info("Processing completed successfully.")


if __name__ == "__main__":
    main()
