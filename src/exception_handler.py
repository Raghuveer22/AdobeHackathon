import os
from zip_data_processing import get_data
from logging_utils import setup_logging
from file_extraction import write_master_data_to_json

BASEPATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
exception_json_path = "exception.json"  # Path to the JSON file for storing exception data
FOLDER = os.path.join(BASEPATH, "Failed")  # Folder containing failed files

def main():
    setup_logging()

    master_data = {}  # Dictionary to store exception data

    for source_file in os.listdir(FOLDER):
        source_file_path = os.path.join(FOLDER, source_file)
        data = get_data(source_file_path, exception=1)  # Get exception data for the file
        master_data[source_file] = data  # Store the exception data in the dictionary

    write_master_data_to_json(master_data=master_data, file_path=exception_json_path)  # Write exception data to JSON file


if __name__ == "__main__":
    main()
