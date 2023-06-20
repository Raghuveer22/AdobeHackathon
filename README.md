# AdobeHackathon# Invoice Processing Project

This project aims to automate the processing of invoices using PDF extraction and data manipulation techniques.

## Project Structure

The project consists of several files:

1. `main.py`: The main script to initiate the processing of PDF files in a source folder.
2. `pdf_operations.py`: Contains functions for PDF extraction and auto-tagging.
3. `zip_data_processing.py`: Contains functions to extract data from the structuredData.json file within a ZIP archive.
4. `logging_utils.py`: Provides logging configuration for the project.
5. `file_extraction.py`: Includes functions to handle file operations such as extracting PDFs and updating master data.
6. `exception_handler.py`: Handles the processing of failed files and generates an exception report.
7. `README.md`: Provides an overview of the project and describes the purpose of each file.

## Usage

1. Place the PDF files to be processed in the source folder specified in `main.py`.
2. Run `main.py` to initiate the processing of the PDF files.
3. The script will extract relevant data from the PDF files, update the master data, and save it in the `invoice.json` file.
4. If any files fail to process initially, the script will retry a maximum number of times specified by `MAX_RETRY_LIMIT` in `main.py`.
5. If the maximum retry limit is reached and there are still failed files, the script will save the list of failed files in `failed_files.txt`.
6. Run `exception_handler.py` to process the failed files separately and generate an exception report in `exception.json`.
7. Review the generated `invoice.json` file for the processed invoice data.
8. Review the `failed_files.txt` file for any files that failed to process within the maximum retry limit.
9. Review the `exception.json` file for the exception report of the failed files.

Note: Make sure to set up the necessary credentials and configurations for the Adobe PDF Services API as described in the project documentation.

## Dependencies

The project relies on the following dependencies:

- `adobe-pdfservices-sdk` (Python SDK for Adobe PDF Services API)
- `openpyxl` (For Excel file manipulation)

Make sure to install the dependencies using the appropriate package manager or `pip`.

## License

This project is licensed under the [MIT License](LICENSE).
![Snake Game](https://raw.githubusercontent.com/trinib/trinib/snake/github-contribution-grid-snake-dark.svg)
