# Setting Up API Credentials Documentation

This documentation provides instructions on how to set up API credentials for interacting with the Adobe PDF Services API.

## Prerequisites
Before setting up API credentials, make sure you have completed the following steps:
- Created a project or have an existing project in the [Adobe Developer Console](https://console.adobe.io/).
- Enabled the "Adobe PDF Services API" for your project.

## Instructions

1. **Generate API Credentials**
   - Access the Adobe Developer Console and navigate to your project.
   - Find the "API Integration" section and select "Credentials".
   - Choose the "JWT" authentication type to generate the API credentials.
   - Provide a unique name for the credentials.
   - Click on the "Generate Key Pair" button to generate the public/private key pair.
   - Save the private key file (`private.key`) securely. This file is required for authenticating API requests.

2. **Create API Credentials JSON File**
   - Create a new JSON file or use an existing one to store your API credentials.
   - Open the JSON file and enter the following credentials:

   ```json
   {
     "client_credentials": {
       "client_id": "<YOUR_CLIENT_ID>",
       "client_secret": "<YOUR_CLIENT_SECRET>"
     },
     "service_account_credentials": {
       "organization_id": "<YOUR_ORGANIZATION_ID>",
       "account_id": "<YOUR_ACCOUNT_ID>",
       "private_key_file": "<PATH_TO_PRIVATE_KEY_FILE>"
     }
   }
   ```

   - Replace `<YOUR_CLIENT_ID>`, `<YOUR_CLIENT_SECRET>`, `<YOUR_ORGANIZATION_ID>`, `<YOUR_ACCOUNT_ID>`, and `<PATH_TO_PRIVATE_KEY_FILE>` with your actual credentials and file path.

3. **Store the API Credentials File**
   - Move the API credentials JSON file to the base folder of your project. This is the same folder where your README file is located.
   - Ensure that the API credentials file is named appropriately, such as `pdfservices-api-credentials.json`.

4. **Update Client Configuration**
   - Locate the `client_config.json` file in your project's `src` folder.
   - Open the `client_config.json` file and update the values based on your requirements and API credentials.

      ```json
        {  
            "connectTimeout": "4000",
            "readTimeout": "20000",
            "region": "eu"
        }
      ```

      - Replace `region`,`connectTimeout`,`readTimeout` with your actual requirements.

5. **Use the API Credentials in Your Project**
   - In your code, import the necessary modules and libraries to use the API credentials.
   - Use the provided functions and methods to load and authenticate with the API credentials.

   ```python
   import os
   from adobe.pdfservices.operation.auth.credentials import Credentials

   # Constants
   BASEPATH = os.path.dirname(os.path.abspath(__file__))
   PDFSERVICEAPICREDENTIALFILEPATH = os.path.join(BASEPATH, 'pdfservices-api-credentials.json')

   # Load and authenticate with the API credentials
   credentials = Credentials.service_account_credentials_builder() \
       .from_file(PDFSERVICEAPICREDENTIALFILEPATH) \
       .build()
   ```

   - Adjust the file paths and imports based on your project structure and requirements.

Congratulations! You have successfully set up your API credentials for the Adobe PDF Services API. You can now integrate and interact with the API using the provided credentials.

Remember to keep your API credentials secure and avoid sharing them publicly.

If you encounter any issues or have further questions, please refer to the official Adobe PDF Services API documentation or seek support from the Adobe Developer Console