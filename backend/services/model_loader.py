from ultralytics import YOLO
import os
from gdown import gdown

def load_model(model_path = None):
    # try:
    #     if model_path is None:
    #         current_dir = os.path.dirname(os.path.abspath(__file__))
    #         model_path = os.path.join(current_dir, '..', 'best_model.pt')
    #     model = YOLO(model_path)
    #     return model
    # except Exception as e: 
    #     print(f"Error while loading model:{e}")
        
    current_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(current_dir, '..', 'best_model.pt')
  
    if not os.path.exists(model_path):
        file_id = os.environ.get('MODEL_ID')
    
        if not file_id:
            return None
        try:
            url = f"https://drive.google.com/uc?id={file_id}"
            gdown.download(url, model_path, quiet = False)
        except Exception as e:
            print(f"Error downloading model: {e}")
            return None    
model = load_model()