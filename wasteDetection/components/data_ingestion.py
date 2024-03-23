from wasteDetection.logger import logging 
from wasteDetection.exception import CustomException
import os ,sys
from wasteDetection.entity.artifacts_entity import DataIngestionArtifacts
from wasteDetection.entity.config_entity import DataIngestionConfig
import zipfile
import gdown



class DataIngestion:
    def __init__(
        self,
        config=DataIngestionConfig
    ):
        try:
            self.config = config
            
        except Exception as e:
            raise CustomException(e,sys)
        
    def download_zip(self):
        try:
            logging.info("downloding zip file")
            
            source_url = self.config.data_download_url
            download_file = self.config.data_ingestion_dir
            os.makedirs(download_file,exist_ok=True)
            
            data_file_name = 'data.zip'
            
            url = source_url.split('/')[-2]
            
            
            
            os.path.join(download_file,data_file_name)
            
            prefix = 'https://drive.google.com/uc?export=download&id='
            gdown.download(prefix+url,data_file_name)
            
            return data_file_name
            
        except Exception as e:
            raise CustomException(e,sys)
        
    def extrate_zip(self,file_path:str):
        try:
            
            logging.info("data is extracting")
            feature_store = self.config.feature_store
            
            os.makedirs(feature_store,exist_ok=True)
            with zipfile.ZipFile(file_path,'r') as f:
                f.extractall(feature_store)
            logging.info("data exctraction is completed")
        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_ingestion(self)-> DataIngestionArtifacts:
        try:
            
            zip_file = self.download_zip()
            feature_store = self.extrate_zip(file_path=zip_file)
            
            
            logging.info("data intiating is stared")
            
            data_ingestion = DataIngestionArtifacts(
                data_zip_file_path=zip_file,
                feature_store_path=feature_store
            )
            
            return data_ingestion
            
            
        except Exception as e:
            raise CustomException(e,sys)