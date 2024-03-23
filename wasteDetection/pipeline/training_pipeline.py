from wasteDetection.logger import logging 
from wasteDetection.exception import CustomException
import os ,sys
from wasteDetection.entity.artifacts_entity import DataIngestionArtifacts
from wasteDetection.entity.config_entity import DataIngestionConfig
from wasteDetection.components.data_ingestion import DataIngestion


class TrainingPipeline:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig
    
    
    def DataIngestionPipeline(self):
        try:
            logging.info("initiong data intation")
            ingestion_obj = DataIngestion(config=self.ingestion_config)
            data_ingetion_artifacts =  ingestion_obj.initiate_data_ingestion()

            return data_ingetion_artifacts
        
            logging.info("data ingestion has initialted")
            
            
        except Exception as e:
            raise CustomException(e,sys)