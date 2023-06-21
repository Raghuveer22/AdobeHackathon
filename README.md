# AdobeHackathon
## Invoice Processing Project

<p align="center">
  <img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" alt="FadingLine">
</p>

This project aims to automate the processing of invoices using PDF extraction and data manipulation techniques.

## Project Structure

After setting up all the files, the project structure will look like this:

```
project/
├── docs/
│   ├── intro.md
│   ├── data_processing.md
│   ├── file_extraction.md
│   ├── zip_data_processing.md
│   ├── pdf_operations.md
│   └── exception.md
├── Master/
│   └── InvoicesData/
│       └── TestDataSet/
├── src/
│   ├── logging_utils.py
│   ├── pdf_operations.py
│   ├── file_extraction.py
│   ├── fail_file_extraction.py
│   ├── exception_handler.py
│   ├── zip_data_processing.py
│   ├── data_processing.py
│   └── client_config.json
├── Failed/
│   └── output81.json (File generated after executing fail_file_extraction.py)
├── pdfservices-api-credentials.json
├── LogFile.log
├── private.key
├── failed_files.txt (File generated after executing file_extraction.py)
├── invoice.json (File generated after executing file_extraction.py)
├── exception.json (File generated after executing exception_handler.py)
├── output.csv (File generated after executing data_processing.py)
└── README.md
```

## Instructions
1. **Obtain the credentials**
   - Go to the [Adobe Developer Console](https://console.adobe.io/) and create a new project or use an existing project.
   - Enable the "Adobe PDF Services API" for your project.
   - Generate the API credentials (JWT authentication) by following the provided documentation and guidelines.
2. **Set Up Project:**
   - Download the private key file and set up the PDF Services API credentials provided by the Adobe Developer Console. For more details, refer to the [`intro.md`](Master\docs\intro.md) file for setup instructions.
   - Move the private key file to the base folder of your project (the same folder where the README file is located).
3. **Update Client Configuration:**
   - Open the `pdf_operations.py` file located in the `src` folder of your project.
   - Update the `PDFSERVICEAPICREDENTIALFILEPATH` value with the relative path to the private key file in the base folder.
   - Make changes to the `client_config.json` file based on your requirements.
4. **Run the Project:**
   - After setting up the private key and updating the client configuration, you are ready to run the project.
   - Follow the provided instructions to run the necessary scripts and initiate the invoice processing.

Make sure to provide clear and specific instructions, and consider adding any additional details or requirements as needed.

## Usage

1. Place the PDF files to be processed in the source folder specified in `file_extraction.py`.
2. Run `file_extraction.py` to initiate the processing of the PDF files.
3. The script will extract relevant data from the PDF files, update the master data, and save it in the `invoice.json` file.
4. If any files fail to process initially, the script will retry a maximum number of times specified by `MAX_RETRY_LIMIT` in `file_extraction.py`.
5. If there is any problem from the user-end like finishing of API quota or network issues, the files will be written into `failed_files.txt`, and you can run `fail_file_extraction.py` directly to process the remaining files after solving the user-end problems.
6. If the maximum retry limit is reached and there are still failed files, the script will save the list of failed files in `failed_files.txt`.
7. Run `exception_handler.py` to process the failed files separately and generate the data in `exception.json`.
8. Review the generated `invoice.json` file for the processed invoice data.
9. Review the `failed_files.txt` file for any files that failed to process within the maximum retry limit.
10. Review the `exception.json` file for the exception report of the failed files.

Note: Make sure to set up the necessary credentials and configurations for the Adobe PDF Services API as described in the project documentation.

## Dependencies

The project relies on the following dependencies:

- `python 3.x`,`adobe-pdfservices-sdk`,`logging` ,`json`,`tempfile`,`csv`,`re`,`zipfile`

Make sure to install the dependencies using the appropriate package manager or `pip`.
<p>
<img src="https://user-images.githubusercontent.com/74038190/216122041-518ac897-8d92-4c6b-9b3f-ca01dcaf38ee.png" alt="Thank You" height="50">
<span>Thanks for visiting!</span></p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/74038190/212741999-016fddbd-617a-4448-8042-0ecf907aea25.gif" alt="Thank You" height="500">
</p>
