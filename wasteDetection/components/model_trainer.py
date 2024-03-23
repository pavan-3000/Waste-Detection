from wasteDetection.logger import logging 
from wasteDetection.exception import CustomException
import os ,sys
from wasteDetection.entity.artifacts_entity import ModelTrainerArtifacts
from wasteDetection.entity.config_entity import ModelTrainerConfig
from wasteDetection.utils.main_utils import read_yaml_fike
import yaml


config = ModelTrainerConfig()
weights = config.weights_name
print(weights)        


class ModelTrainer:
    def __init__(self,config:ModelTrainerConfig):
        self.config  = config
        self.weights = self.config.weights_name
        
    def Train(self)-> ModelTrainerArtifacts:
        try:
            
            logging.info("modifing the model")
            
            with open('/home/snow/Music/Waste-Detection/artifacts/data_ingestion/feature_store/test.v2i.yolov5pytorch/data.yaml','r') as f:
                no_classes = str(yaml.safe_load(f)['nc'])
            print(no_classes)
            model_config = self.config.weights_name.split(".")[0]
            logging.info("weight is initialted")
            print(f"model = {model_config}")
            
            
            modele_config  = read_yaml_fike(f"yolov5/models/{model_config}.yaml")
            modele_config['nc'] = int(no_classes)
            
            with open(f'yolov5/models/custom_{model_config}.yaml','w') as f:
                yaml.dump(modele_config,f)
            
            
            logging.info("model is saved")
                
            data = "/home/snow/Music/Waste-Detection/artifacts/data_ingestion/feature_store/test.v2i.yolov5pytorch/data.yaml"   
            os.system(f'cd yolov5/ && python train.py --img 640 --batch {self.config.batch_size} --epochs {self.config.epochs} --weights {self.config.weights_name} --name yolo_result --cfg ./models/custom_yolov5s.yaml --data {data} --cache')
            os.system("cp yolov5s/runs/train/yolo_result/weights/best.pt yolov/5")
            os.makedirs(self.config.model_trainer_dir,exist_ok=True)
            os.system(f"cp yolov5s/runs/train/yolo_result/weights/best.pt {self.config.model_trainer_dir}")
            
            model_artifacts = ModelTrainerArtifacts(
                trained_model_path="yolov5s/best.pt"
            )
            
            logging.info("model trined is sucessfull")
            
        except Exception as e:
            raise CustomException(e,sys)
        
        
