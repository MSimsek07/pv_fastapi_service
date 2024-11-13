import logging
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.efficientnet import preprocess_input
import os
import io

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

def load_model():
    """Load the pre-trained model from the specified path."""
    model_path = os.getenv('MODEL_PATH', 'model_efficientnet.h5')
    logger.info(f"Loading model from {model_path}")
    return tf.keras.models.load_model(model_path)

model = load_model()

def process_image(uploaded_image):
    """Process the uploaded image to the format required by the model."""
    logger.info("Processing image")
    img = image.load_img(io.BytesIO(uploaded_image), target_size=(224, 224))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    return preprocess_input(img)

def predict_image(model, img):
    """Make a prediction using the model on the processed image."""
    logger.info("Making prediction")
    prediction = model.predict(img)
    return prediction

pv_labels = {
    0: 'Cell', 1: 'Cell-Multi', 2: 'Cracking', 3: 'Diode', 4: 'Diode-Multi', 
    5: 'No-Anomaly', 6: 'Offline-Module', 7: 'Shadowing', 8: 'Soiling', 9: 'Vegetation'
}

def get_prediction_percentages(predictions):
    """Convert model predictions to percentage probabilities."""
    logger.info("Converting predictions to percentages")
    total = sum(predictions)
    percentages = {pv_labels[i]: round((pred / total) * 100, 2) for i, pred in enumerate(predictions)}
    return percentages

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    """API endpoint to predict the class of the uploaded image."""
    logger.info("Received prediction request")
    contents = await file.read()
    img = process_image(contents)
    prediction = predict_image(model, img)
    
    percentages = get_prediction_percentages(prediction[0])
    response = {
        "percentages": percentages
    }
    logger.info(f"Prediction response: {response}")
    return JSONResponse(content=response)