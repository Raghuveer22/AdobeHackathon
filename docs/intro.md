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

### Now run the code as described in [`README.md`](../../README.md)