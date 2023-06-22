To obtain the credentials for Adobe PDF Services API and set up your project, follow these steps:

1. **Obtain the Credentials:**

   - Go to the [Adobe Developer Console](https://console.adobe.io/) and register for Adobe Cloud Services if you haven't done so already.
   - Create a new project or use an existing project. Enable the "Adobe PDF Services API" for your project.
   - Generate a key pair and save the configured API.
   - Visit the service account JWT credentials for your account details.

2. **Set Up Project:**

   - Download the configuration zip file and extract the private key from it. This private key is provided by the Adobe Developer Console. 
   - Move the private key file to the base folder of your project, where the README file is located.

3. **Create API Credentials JSON File:**

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

4. **Store the API Credentials File:**

   - Move the API credentials JSON file to the base folder of your project, where the README file is located.
   - Make sure to name the API credentials file appropriately, such as `pdfservices-api-credentials.json`.

5. **Update Client Configuration:**

   - Open the `pdf_operations.py` file located in the `src` folder of your project.
   - Modify the `client_config.json` file based on your requirements. You can find it in the `src` folder.

   ```json
   {
     "connectTimeout": "4000",
     "readTimeout": "20000",
     "region": "eu"
   }
   ```

   - Replace `region`, `connectTimeout`, and `readTimeout` with your desired values.


*make sure to make output folder in the root if not exists and failed folder in the output folder for the code to work*
By following these steps, you should have obtained the credentials, set up your project, and updated the client configuration.

### Now run the code as described in [`README.md`](../README.md)
