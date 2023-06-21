import os
import json
import logging
import zipfile
from logging_utils import setup_logging
from pdf_operations import create_execution_context, extract_pdf, get_auto_tag_pdf
from zip_data_processing import extract_and_process

# Set the base path of the project
BASEPATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def process_pdf(source_file_path, execution_context):
    """
    Extracts PDF and processes its contents.

    Args:
        source_file_path (str): The path of the source PDF file.
        execution_context (ExecutionContext): The execution context for API operations.

    Returns:
        dict or None: The processed data as a dictionary, or None if an exception occurs.
    """
    result_file_path = extract_pdf(source_file_path=source_file_path, execution_context=execution_context)
    if result_file_path is not None:
        return extract_and_process(zip_file_path=result_file_path)
    else:
        return None


def process_files(source_folder, execution_context):
    """
    Processes all PDF files in the source folder.

    Args:
        source_folder (str): The path of the source folder containing PDF files.
        execution_context (ExecutionContext): The execution context for API operations.

    Returns:
        tuple: A tuple containing the master data dictionary and a list of failed files.
    """
    master_data = {}  # Dictionary to store processed data
    failed_files = []  # List to store files that failed to process
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


def update_master_data_with_failed_files(master_data, source_folder, failed_files, execution_context):
    """
    Retry processing failed files with auto-tagged PDFs and update the master data.

    Args:
        master_data (dict): The dictionary containing the master data.
        source_folder (str): The path of the source folder containing the failed files.
        failed_files (list): The list of files that failed to process.
        execution_context (ExecutionContext): The execution context for API operations.

    Returns:
        dict: The updated master data dictionary.
    """
    missed_data = {}  # Dictionary to store processed data from failed files
    for failed_file in failed_files:
        source_file_path = os.path.join(source_folder, failed_file)
        tagged_pdf_path = get_auto_tag_pdf(execution_context=execution_context, source_file_path=source_file_path)
        if tagged_pdf_path is not None:
            result_file_path = extract_pdf(source_file_path=tagged_pdf_path, execution_context=execution_context)
            if result_file_path is not None:
                data = extract_and_process(zip_file_path=result_file_path)
                if data is not None:
                    missed_data[failed_file] = data
    master_data.update(missed_data)
    return master_data


def write_master_data_to_json(master_data, file_path):
    """
    Writes the master data dictionary to a JSON file.

    Args:
        master_data (dict): The master data dictionary.
        file_path (str): The path of the JSON file to write.
    """
    with open(file_path, 'w') as file:
        json.dump(master_data, file)


def write_failed_files(failed_files, file_path):
    """
    Writes the list of failed files to a text file.

    Args:
        failed_files (list): The list of failed file names.
        file_path (str): The path of the text file to write.
    """
    with open(file_path, 'w') as file:
        for failed_file in failed_files:
            file.write(failed_file + '\n')


def save_json(file, source_folder, save_folder, execution_context):
    """
    Saves a JSON file from an auto-tagged PDF.

    Args:
        file (str): The name of the PDF file.
        source_folder (str): The path of the source folder containing the PDF file.
        save_folder (str): The path of the folder to save the JSON file.
        execution_context (ExecutionContext): The execution context for API operations.

    Returns:
        int: The status code indicating the success or failure of file processing.
    """
    source_file_path = os.path.join(source_folder, file)
    tagged_pdf_path = get_auto_tag_pdf(execution_context=execution_context, source_file_path=source_file_path)
    if tagged_pdf_path is not None:
        result_file_path = extract_pdf(source_file_path=tagged_pdf_path, execution_context=execution_context)
    file_name, _ = file.split(".")
    new_file_name = file_name + ".json"
    if result_file_path is not None:
        with zipfile.ZipFile(result_file_path, 'r') as zip_file:
            extracted_file_name = zip_file.namelist()[0]  # Get the name of the first extracted file
            extracted_file_path = os.path.join(save_folder, extracted_file_name)
            zip_file.extractall(path=save_folder)
        try:
            new_file_path = os.path.join(save_folder, new_file_name)
            if os.path.exists(new_file_path):
                os.remove(new_file_path)  # Remove the existing file at new_file_path
            os.rename(extracted_file_path, new_file_path)  # Rename the extracted file to the desired name
            return 200  
        except Exception as e:
            logging.error(f"An error occurred: {str(e)}")
            return 500  # Indicate an error occurred during file processing
    else:
        return 404  # Indicate file not found


MAX_RETRY_LIMIT = 3
json_file = os.path.join("output","invoice.json")
failed_file = os.path.join("output","failed_files.txt")


def main():
    """
    The main function to execute the PDF processing workflow.
    """
    setup_logging()
    execution_context = create_execution_context()
    source_folder = os.path.join(BASEPATH, 'InvoicesData', 'TestDataSet')
    master_data, failed_files = process_files(source_folder, execution_context)
    write_master_data_to_json(master_data, json_file)
    retry_count = 0
    while failed_files and retry_count < MAX_RETRY_LIMIT:
        master_data = update_master_data_with_failed_files(master_data, source_folder, failed_files, execution_context)
        write_master_data_to_json(master_data, json_file)
        failed_files = [file for file in failed_files if file not in master_data]
        retry_count += 1

    if failed_files:
        write_failed_files(failed_files, failed_file)
        logging.error("Failed to process some files after reaching the maximum retry limit. "
                      "The list of failed files has been saved to 'failed_files.txt'.")
    logging.info("Processing completed successfully.")


if __name__ == "__main__":
    main()
