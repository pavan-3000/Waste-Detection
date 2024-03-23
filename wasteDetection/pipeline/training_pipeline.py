from wasteDetection.logger import logging 
from wasteDetection.exception import CustomException
import os ,sys
from wasteDetection.entity.artifacts_entity import DataIngestionArtifacts,ModelTrainerArtifacts
from wasteDetection.entity.config_entity import DataIngestionConfig,ModelTrainerConfig
from wasteDetection.components.data_ingestion import DataIngestion
from wasteDetection.components.model_trainer import ModelTrainer


class TrainingPipeline:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig
        self.model_config = ModelTrainerConfig
    
    
    def DataIngestionPipeline(self):
        try:
            logging.info("initiong data intation")
            ingestion_obj = DataIngestion(config=self.ingestion_config)
            data_ingetion_artifacts =  ingestion_obj.initiate_data_ingestion()

            return data_ingetion_artifacts
        
            logging.info("data ingestion has initialted")
            
            
        except Exception as e:
            raise CustomException(e,sys)
        
    def ModelTrainerPipeline(self) -> ModelTrainerArtifacts:
        try:
            logging.info("initing model traienr")
            
            model_trainer = ModelTrainer(
                config=self.model_config
            )
            model_trainer_artifacts = model_trainer.Train()
            
            
            return model_trainer_artifacts
            
        except Exception as e:
            raise CustomException(e,sys)