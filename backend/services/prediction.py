from .model_loader import model
from PIL import Image
import io
import base64

import gc 

def get_prediction(img_bytes):
    if model is None:
        raise ValueError("Model unloaded.")
    
    try:
        img = Image.open(io.BytesIO(img_bytes))
        print(f"Image mode: {img.mode}, size: {img.size}")
        result = model(img)
        print(f"Model inference result: {result}")
    except Exception as e:
        print(f"Error during prediction: {e}")
        raise ValueError("Invalid image data.")
    
    img_with_boxes = result[0].plot()
    img_result = Image.fromarray(img_with_boxes[..., :: -1])

    buf = io.BytesIO()
    img_result.save(buf, format = "JPEG")    
    img_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
    
    detections = []
    conf_threshold = 0.25
    for box in result[0].boxes:
        confidence = float(box.conf[0])
        class_id = int(box.cls[0])
        if confidence >= conf_threshold:
            print(f"Detected {model.names[class_id]} with confidence {confidence}")
            detections.append({
                "class": model.names[class_id],
                "confidence": round(confidence, 2)
            })
        else:
            print(f"Ignored noise with confidence {confidence}")
            continue
    
    del img, result, img_with_boxes, img_result, buf
    gc.collect()
    print(f"Resulting detections: {detections}")
    return {
        "image_base64": img_base64,
        "detections": detections
    }
                           
       