# PDF Operations Documentation

This module provides functions for performing various operations on PDF files using Adobe PDF Services API. The operations include extracting text from a PDF and autotagging a PDF.

## Table of Contents
- [Dependencies](#dependencies)
- [Constants](#constants)
- [Functions](#functions)
  - [create_execution_context()](#create_execution_context)
  - [extract_pdf(execution_context, source_file_path)](#extract_pdf)
  - [get_auto_tag_pdf(execution_context, source_file_path)](#get_auto_tag_pdf)

## Dependencies

This module relies on the following dependencies:
- `os`
- `logging`
- `tempfile`
- `os`
- `adobe-pdfserivices-sdk`

Make sure to install the required dependencies to use this module.

## Constants

- `BASEPATH`: The base path of the project directory. It is determined dynamically based on the location of the current script file.
- `CLIENTCONFIGFILE`: The path to the client configuration file (`client_config.json`) located in the `src` directory.
- `PDFSERVICEAPICREDENTIALFILEPATH`: The path to the PDF Services API credentials file (`pdfservices-api-credentials.json`) located in the project directory.

## Functions

### `create_execution_context()`

This function creates an execution context for interacting with the Adobe PDF Services API. It reads the credentials from the PDF Services API credentials file and builds the execution context.

Returns:
- `execution_context` (ExecutionContext): The created execution context.

### `extract_pdf(execution_context, source_file_path)`

This function extracts text from a PDF file using the Adobe PDF Services API.

Parameters:
- `execution_context` (ExecutionContext): The execution context for interacting with the API.
- `source_file_path` (str): The path to the source PDF file to extract text from.

Returns:
- `temp_file_path` (str): The path to the temporary ZIP file containing the extracted text.

### `get_auto_tag_pdf(execution_context, source_file_path)`

This function performs autotagging on a PDF file using the Adobe PDF Services API.

Parameters:
- `execution_context` (ExecutionContext): The execution context for interacting with the API.
- `source_file_path` (str): The path to the source PDF file to perform autotagging on.

Returns:
- `temp_file_path` (str): The path to the temporary autotagged PDF file.

---

This module provides convenient functions to

 interact with the Adobe PDF Services API and perform PDF operations. Use the provided functions in your project to extract text from PDF files and perform autotagging on PDF files.

Please refer to the project documentation for detailed usage instructions.

[Please let me know if you need any further assistance or have any questions!](https://github.com/Raghuveer22/AdobeHackathon/issues)
