# PDF Data Processing Documentation

This documentation provides an overview and instructions for using the code to process PDF files, extract data, and save the results in a JSON file.

## Code Overview

The provided code consists of several functions and utility methods:

- `process_pdf(source_file_path, execution_context)`: This function extracts data from a PDF file using the `extract_pdf` function and processes its contents using the `extract_and_process` function. It returns the processed data as a list.

- `process_files(source_folder, execution_context)`: This function processes all PDF files in a specified folder. It calls `process_pdf` for each file and collects the processed data into a dictionary. It also tracks any failed files in a separate list.

- `update_master_data_with_failed_files(master_data, source_folder, failed_files, execution_context)`: This function retries processing the failed files by attempting to extract and process their auto-tagged PDF versions. It updates the `master_data` dictionary with the processed data from the failed files.

- `write_master_data_to_json(master_data, file_path)`: This function writes the `master_data` dictionary to a JSON file at the specified `file_path`.

- `write_failed_files(failed_files, file_path)`: This function writes the list of failed files to a text file at the specified `file_path`.

- `save_json(file, source_folder, save_folder, execution_context)`: This function saves a JSON file from an auto-tagged PDF. It extracts the processed data from the PDF and renames it to the desired file name in the specified `save_folder`.

- `main()`: This is the main function that orchestrates the PDF processing workflow. It sets up logging, creates an execution context using `create_execution_context`, processes the PDF files in the specified source folder using `process_files`, updates the data from failed files using `update_master_data_with_failed_files`, and finally writes the results to JSON using `write_master_data_to_json`.

## Instructions

Follow these instructions to use the code for PDF data processing:

1. **Import Dependencies**: Ensure that you have the necessary dependencies installed. The code relies on modules such as `os`, `json`, `logging`, and `zipfile`. Install any missing dependencies using your preferred package manager or `pip`.

2. **Logging Configuration**: The code uses a custom logging configuration from a module called `logging_utils`. Make sure you have the `logging_utils.py` file in the same directory as your main script or adjust the import statement accordingly.

3. **Setup API Credentials**: Make sure you have set up your API credentials by following the documentation provided earlier. This ensures that the code can access the necessary Adobe PDF Services API.

4. **Specify File Paths**: Update the `BASEPATH` variable to reflect the base path of your project. Modify the `json_file` and `failed_file` variables to specify the desired file names for the JSON file and the file containing failed file names, respectively.

5. **Specify Source Folder**: Update the `source_folder` variable to point to the folder containing the PDF files you want to process.

6. **Run the Script**: Execute the `main()` function to start the PDF processing workflow. The script will process the PDF files, extract data, handle failed files, and save the results in the specified JSON file.

```python
if __name__ == "__main__":
    main()
```

7. **Review Output**: After the script completes, you can review the generated JSON file containing the processed data. If any files failed to process after reaching the maximum retry limit, the list of failed files will be saved to the specified text file.

8. **Additional Customization**: Feel free to customize the code further to fit your project's specific requirements. You

 can modify the data extraction and processing logic, adjust the logging behavior, or enhance the error handling based on your needs.

## Conclusion

With the provided code and instructions, you can automate the processing of PDF files, extract relevant data, and save the results in a JSON format. Modify and extend the code as required to suit your specific use case.

If you encounter any issues or have further questions, refer to the code comments or seek assistance from the appropriate channels or resources.