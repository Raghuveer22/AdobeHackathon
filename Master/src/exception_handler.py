import os
from zip_data_processing import get_data
from logging_utils import setup_logging
from file_extraction import write_master_data_to_json
BASEPATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
exception_json_path="exception.json"
FOLDER=os.path.join(BASEPATH,"Master","Failed")
def main():
    setup_logging()
    master_data={}
    for source_file in os.listdir(FOLDER):
        source_file_path=os.path.join(FOLDER,source_file)
        data=get_data(source_file_path,exeception=1)
        master_data[source_file]=data
    write_master_data_to_json(master_data=master_data,file_path=exception_json_path)
    
    
if __name__=="__main__":
    main()
