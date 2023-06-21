# PDF Processing Workflow

This script implements a PDF processing workflow that extracts data from PDF files and generates JSON files as output. The workflow involves extracting data from PDF files, processing the extracted data, and handling failed files by retrying with auto-tagged PDFs.

## Table of Contents
- [Dependencies](#dependencies)
- [Functions](#functions)
  - [process_pdf(source_file_path, execution_context)](#process_pdf)
  - [process_files(source_folder, execution_context)](#process_files)
  - [update_master_data_with_failed_files(master_data, source_folder, failed_files, execution_context)](#update_master_data_with_failed_files)
  - [write_master_data_to_json(master_data, file_path)](#write_master_data_to_json)
  - [write_failed_files(failed_files, file_path)](#write_failed_files)
  - [save_json(file, source_folder, save_folder, execution_context)](#save_json)
- [Main Workflow](#main-workflow)

## Dependencies

This script relies on the following dependencies:
- `os`
- `json`
- `logging`
- `zipfile`
- `logging_utils`
- `pdf_operations`
- `zip_data_processing`

Make sure to install the required dependencies to run this script.

## Functions

### `process_pdf(source_file_path, execution_context)`

This function extracts the contents of a PDF file and processes them.

Parameters:
- `source_file_path` (str): The path of the source PDF file.
- `execution_context` (ExecutionContext): The execution context for API operations.

Returns:
- `data` (dict or None): The processed data as a dictionary, or None if an exception occurs.

### `process_files(source_folder, execution_context)`

This function processes all the PDF files in a given folder.

Parameters:
- `source_folder` (str): The path of the source folder containing the PDF files.
- `execution_context` (ExecutionContext): The execution context for API operations.

Returns:
- `master_data` (dict): The dictionary containing the processed data for each PDF file.
- `failed_files` (list): The list of files that failed to process.

### `update_master_data_with_failed_files(master_data, source_folder, failed_files, execution_context)`

This function retries processing the failed files using auto-tagged PDFs and updates the master data.

Parameters:
- `master_data` (dict): The dictionary containing the master data.
- `source_folder` (str): The path of the source folder containing the failed files.
- `failed_files` (list): The list of files that failed to process.
- `execution_context` (ExecutionContext): The execution context for API operations.

Returns:
- `master_data` (dict): The updated master data dictionary.

### `write_master_data_to_json(master_data, file_path)`

This function writes the master data dictionary to a JSON file.

Parameters:
- `master_data` (dict): The master data dictionary.
- `file_path` (str): The path of the JSON file to write.

### `write_failed_files(failed_files, file_path)`

This function writes the list of failed files to a text file.

Parameters:
- `failed_files` (list): The list of failed file names.
- `file_path` (str): The path of the text file to write.

### `save_json(file, source_folder, save_folder, execution_context)`

This function saves a JSON file generated from an auto-tagged PDF.

Parameters:
- `file` (str): The name of the PDF file.
- `source_folder` (str): The path of the source folder containing the PDF file.
- `save_folder` (str): The path of the folder to save the JSON file.


- `execution_context` (ExecutionContext): The execution context for API operations.

Returns:
- `status_code` (int): The status code indicating the success or failure of file processing.

## Main Workflow

The script provides a main function that executes the PDF processing workflow. The main function performs the following steps:
1. Sets up logging.
2. Creates the execution context for API operations.
3. Defines the source folder containing the PDF files.
4. Processes the PDF files in the source folder and retrieves the master data dictionary and the list of failed files.
5. Writes the master data dictionary to a JSON file.
6. Retries processing the failed files with auto-tagged PDFs and updates the master data.
7. Writes the updated master data dictionary to the JSON file.
8. Handles cases where some files failed to process after reaching the maximum retry limit, and writes the list of failed files to a text file.
9. Logs the completion of the processing.

To use this script, ensure that the required dependencies are installed and set the appropriate values for the `BASEPATH` and other variables according to your project's structure and requirements. Run the script to start the PDF processing workflow.

Refer to the project documentation for detailed usage instructions and examples.

Please let me know if you need any further assistance or have any questions!