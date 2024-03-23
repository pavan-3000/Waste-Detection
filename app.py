from wasteDetection.logger import logging
from wasteDetection.exception import CustomException

import os,sys
from wasteDetection.pipeline.training_pipeline import TrainingPipeline

try:
    
    logging.info("data ingestion has stared")
    ingestion_obj = TrainingPipeline()
    ingestion_obj.DataIngestionPipeline()
    logging.info("data ingestion has completed")
except Exception as e:
    raise CustomException(e,sys)