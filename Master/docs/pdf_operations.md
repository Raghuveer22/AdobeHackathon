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
- `os.path`
- `pathlib`
- `adobe.pdfservices.operation.auth.credentials.Credentials`
- `adobe.pdfservices.operation.client_config.ClientConfig`
- `adobe.pdfservices.operation.pdfops.options.extractpdf.extract_pdf_options.ExtractPDFOptions`
- `adobe.pdfservices.operation.pdfops.options.extractpdf.extract_element_type.ExtractElementType`
- `adobe.pdfservices.operation.execution_context.ExecutionContext`
- `adobe.pdfservices.operation.pdfops.extract_pdf_operation.ExtractPDFOperation`
- `adobe.pdfservices.operation.auth.credentials.Credentials`
- `adobe.pdfservices.operation.exception.exceptions.ServiceApiException`
- `adobe.pdfservices.operation.exception.exceptions.ServiceUsageException`
- `adobe.pdfservices.operation.exception.exceptions.SdkException`
- `adobe.pdfservices.operation.execution_context.ExecutionContext`
- `adobe.pdfservices.operation.io.file_ref.FileRef`
- `adobe.pdfservices.operation.pdfops.options.autotagpdf.autotag_pdf_options.AutotagPDFOptions`
- `adobe.pdfservices.operation.internal.api.dto.request.autotagpdf.autotag_pdf_output.AutotagPDFOutput`
- `adobe.pdfservices.operation.pdfops.autotag_pdf_operation.AutotagPDFOperation`
- `adobe.pdfservices.operation.pdfops.options.extractpdf.table_structure_type.TableStructureType`

Make sure to install the required dependencies to use this module.

## Constants

- `BASEPATH`: The base path of the project directory. It is determined dynamically based on the location of the current script file.
- `CLIENTCONFIGFILE`: The path to the client configuration file (`client_config.json`) located in the `Master/src` directory.
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

Please refer to the project documentation for detailed usage instructions and examples.

Feel free to reach out if you have any questions or need further assistance.

