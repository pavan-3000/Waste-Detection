from wasteDetection.logger import logging 
from wasteDetection.exception import CustomException
import os ,sys
from wasteDetection.entity.artifacts_entity import ModelTrainerArtifacts
from wasteDetection.entity.config_entity import ModelTrainerConfig
from wasteDetection.utils.main_utils import read_yaml_fike,read_yaml
import yaml


try:
    config = ModelTrainerConfig()
    model_config = config.weights_name
    
    print(model_config)
    with open('/home/snow/Music/Waste-Detection/artifacts/data_ingestion/feature_store/test.v2i.yolov5pytorch/data.yaml','r') as f:
                no_classes = str(yaml.safe_load(f)['nc'])
    print(type(no_classes))
    no_classes = int(no_classes)
    print(type(no_classes))
   
    model_config = config.weights_name.split(".")[0]
    logging.info("weight is initialted")
    print(model_config)
            

except Exception as e:
    raise CustomException(e,sys)

