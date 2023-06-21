import os
import logging
import tempfile
from adobe.pdfservices.operation.auth.credentials import Credentials
from adobe.pdfservices.operation.client_config import ClientConfig
from adobe.pdfservices.operation.pdfops.options.extractpdf.extract_pdf_options import ExtractPDFOptions
from adobe.pdfservices.operation.pdfops.options.extractpdf.extract_element_type import ExtractElementType
from adobe.pdfservices.operation.execution_context import ExecutionContext
from adobe.pdfservices.operation.pdfops.extract_pdf_operation import ExtractPDFOperation
from adobe.pdfservices.operation.auth.credentials import Credentials
from adobe.pdfservices.operation.exception.exceptions import ServiceApiException, ServiceUsageException, SdkException
from adobe.pdfservices.operation.execution_context import ExecutionContext
from adobe.pdfservices.operation.io.file_ref import FileRef
from adobe.pdfservices.operation.internal.api.dto.request.autotagpdf.autotag_pdf_output import AutotagPDFOutput
from adobe.pdfservices.operation.pdfops.autotag_pdf_operation import AutotagPDFOperation

# Constant Literals
BASEPATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CLIENTCONFIGFILE = os.path.join(BASEPATH, 'Master', 'src', 'client_config.json')
PDFSERVICEAPICREDENTIALFILEPATH = os.path.join(BASEPATH, 'pdfservices-api-credentials.json')

# Tuple of exceptions
EXCEPTIONS = (ServiceApiException, ServiceUsageException, SdkException)
EXCEPTIONLOG = "Exception encountered while executing operation"

def create_execution_context():
    """
    Creates an execution context using Adobe PDF Services credentials and client configuration.

    Returns:
        ExecutionContext or None: The created execution context or None if an exception occurs.
    """
    try:
        credentials = Credentials.service_account_credentials_builder() \
            .from_file(PDFSERVICEAPICREDENTIALFILEPATH) \
            .build()
        client_config = ClientConfig.builder().build()
        execution_context = ExecutionContext.create(credentials, client_config)
        return execution_context
    except EXCEPTIONS as e:
        logging.exception(f"{EXCEPTIONLOG}, {e}")
        return None

def extract_pdf(execution_context, source_file_path):
    """
    Extracts text elements from a PDF file using the Adobe PDF Services SDK.

    Args:
        execution_context (ExecutionContext): The execution context for API operations.
        source_file_path (str): The path of the source PDF file.

    Returns:
        str or None: The path of the temporary zip file containing the extracted text elements,
                    or None if an exception occurs.
    """
    try: 
        extract_pdf_operation = ExtractPDFOperation.create_new()
        source = FileRef.create_from_local_file(source_file_path)
        extract_pdf_operation.set_input(source)
        extract_pdf_options: ExtractPDFOptions = ExtractPDFOptions.builder() \
                                                .with_elements_to_extract([ExtractElementType.TEXT]) \
                                                .build()
        extract_pdf_operation.set_options(extract_pdf_options)
        if execution_context is not None:
            result = extract_pdf_operation.execute(execution_context)
            temp_file_path = tempfile.mktemp(suffix='.zip')
            result.save_as(temp_file_path)
            return temp_file_path
        else:
            logging.exception("The execution context received is None")
    except EXCEPTIONS as e:
        logging.exception(f"{EXCEPTIONLOG}, {e}")
        return None
    
def get_auto_tag_pdf(execution_context, source_file_path):
    """
    Performs auto-tagging of a PDF file using the Adobe PDF Services SDK.

    Args:
        execution_context (ExecutionContext): The execution context for API operations.
        source_file_path (str): The path of the source PDF file.

    Returns:
        str or None: The path of the temporary tagged PDF file, or None if an exception occurs.
    """
    try:
        autotag_pdf_operation = AutotagPDFOperation.create_new()
        source = FileRef.create_from_local_file(source_file_path)
        autotag_pdf_operation.set_input(source)
        if execution_context is not None:
            autotag_pdf_output: AutotagPDFOutput = autotag_pdf_operation.execute(execution_context)
            temp_file_path = tempfile.mktemp(suffix='.pdf')
            autotag_pdf_output.get_tagged_pdf().save_as(temp_file_path)
            return temp_file_path
    except EXCEPTIONS as e:
        logging.exception(f"{EXCEPTIONLOG}, {e}")
        return None
