## Fail File Extraction and Exception Handling

This project consists of two Python scripts: `fail_file_extraction.py` and `exception_handler.py`. These scripts handle the extraction of failed files and exception data, respectively.

### `fail_file_extraction.py`

This script is responsible for extracting failed files and performing retries for a specified maximum number of attempts.

#### Usage:

1. Ensure that the necessary dependencies and libraries are installed.
2. Update the file paths and constants as needed:

   - `BASEPATH`: The base directory path of your project.
   - `json_file`: The path to the JSON file storing master data.
   - `failed_files_path`: The path to the text file storing failed file names.
   - `MAX_RETRY_LIMIT`: The maximum number of retry attempts for failed files.

3. Run the script using a Python interpreter.

#### Steps performed by the script:

1. Sets up logging for the script.
2. Defines the source folder path for invoice data and creates an execution context.
3. Loads the master data from a JSON file.
4. Loads the failed file names from a text file.
5. Executes a loop to retry failed files until the maximum retry limit is reached or all files are processed successfully.
6. Updates the master data with the failed files and writes it back to the JSON file.
7. Removes the processed files from the failed files list.
8. If there are still failed files remaining, attempts to process them again and extracts json data of them to a ["Failed"](../output/failed/) folder.
9. Writes the list of failed files to a text file.
10. Logs the completion of the processing.

### `exception_handler.py`

This script handles the extraction of exception data for files that failed during processing.

#### Usage:

1. Ensure that the necessary dependencies and libraries are installed.
2. Update the file paths and constants as needed:

   - `BASEPATH`: The base directory path of your project.
   - `FAILEDFILESFOLDER`: The folder containing failed files.
   - `exception_json_path`: The path to the JSON file for storing exception data.

3. Run the script using a Python interpreter.

#### Steps performed by the script:

1. Sets up logging for the script.
2. Creates an empty dictionary to store the exception data.
3. Iterates through the failed files in the specified folder.
4. Retrieves exception data for each file using the `get_data` function from the `zip_data_processing` module.
5. Stores the exception data in the dictionary using the file name as the key.
6. Writes the exception data to a JSON file using the `write_master_data_to_json` function.
7. Logs the completion of the exception handling.
