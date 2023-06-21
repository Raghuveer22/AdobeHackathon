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
