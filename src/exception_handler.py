import os
from zip_data_processing import get_data
from logging_utils import setup_logging
from file_extraction import write_master_data_to_json

BASEPATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FAILEDFILESFOLDER = os.path.join(BASEPATH,"output","failed")  # Folder containing failed files
exception_json_path =os.path.join(BASEPATH,"output","exception.json") # Path to the JSON file for storing exception data

def main():
    setup_logging()

    missed_data = {}  # Dictionary to store exception data
    for source_file in os.listdir(FAILEDFILESFOLDER):
        source_file_path = os.path.join(FAILEDFILESFOLDER, source_file)
        data = get_data(source_file_path, exception=1)  # Get exception data for the file
        missed_data[source_file] = data  # Store the exception data in the dictionary

    write_master_data_to_json(master_data=missed_data, file_path=exception_json_path)  # Write exception data to JSON file


if __name__ == "__main__":
    main()
