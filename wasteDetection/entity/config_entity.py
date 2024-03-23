from dataclasses import dataclass 
import os

from wasteDetection.constant.training_pipeline import *

@dataclass
class trainingpipe:
    artifacts_dir = ARTIFACTS_DIR
  
  
training_config:trainingpipe = trainingpipe()  



@dataclass
class DataIngestionConfig:
    data_ingestion_dir = os.path.join(
        training_config.artifacts_dir,DATA_INGESTION_DIR
    )
    
    
    
    feature_store = os.path.join(
        data_ingestion_dir,FEATURE_STORE_FILE_PATH
    )
    
    
    data_download_url = DATA_DOWNLOAD_URL
    

@dataclass
class ModelTrainerConfig:
    
    model_trainer_dir = os.path.join(
        trainingpipe.artifacts_dir,MODEL_TRAINER_DIR

    )
    batch_size = MODEL_BATCH_SIZE
    epochs = MODEL_EPOCHS
    weights_name = MODEL_WEIGHTS
    