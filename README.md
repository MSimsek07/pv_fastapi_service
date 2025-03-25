## FastAPI Application for Photovoltaic Panel Anomaly Detection

This document analyzes the source code of a FastAPI application that deploys a machine learning model developed to detect anomalies in a photovoltaic (PV) panel image. The application allows users to upload an image of a PV panel and receive a response with the percentage of anomaly types predicted by the model.

#### Programming Language

The application is developed using **FastAPI**, a modern and fast Python web framework for building web APIs. It also uses **TensorFlow** and **Keras** for machine learning model training and prediction.

#### Overview

The application consists of a single API endpoint that processes an uploaded image, makes predictions using a pre-trained TensorFlow model and returns the results in a user-friendly JSON format.

### Main Components

The application consists of the following basic components:

1. **`load_model()` Function:** This function loads the pre-trained machine learning model from a specified path. The model path can be configured using an environment variable (`MODEL_PATH`), which is set to “model_efficientnet.h5” by default.

2. **`process_image()` Function:** This function takes the loaded image, loads it from the byte array, resizes it to the size expected by the model (224x224), converts it to a NumPy array and preprocesses it to match the input requirements of the model.

3. **`predict_image()` Function:** This function takes the processed image as input and performs a prediction using the preloaded model. The prediction is returned as an array containing the probabilities for each anomaly class.

4. **`get_prediction_percentages()` Function:** This function takes the model's predictions and converts them into percentage probabilities for each anomaly class. It then returns the results in a dictionary with user-friendly labels.

5. **`/predict/` Endpoint:** This is the main API endpoint where the application accepts a POST request. The endpoint waits for an uploaded image file (called a `file'). When the request is received, the image is processed using the `process_image()` function, a prediction is made using the `predict_image()` function, and the results are converted to percentages using the `get_prediction_percentages()` function. Finally, a JSON response with the prediction percentages is returned to the client.

### API Endpoints

The application offers a single API endpoint, described below:

**POST /predict/**

* Purpose:** Used to estimate anomalies in an uploaded PV panel image.
* Request Body:** Multipart/form data named “file” containing the uploaded image file.
* Answer:** A JSON object containing the predicted anomaly types and their corresponding percentage probabilities.
     ```json
     {
         “percentages": {
             “Cell": 10.5,
             “Cell-Multi": 2.3,
             “Cracking": 0.1,
             “Diode": 5.7,
             “Diode-Multi": 0.8,
             “No-Anomaly": 75.2,
             “Offline-Module": 1.9,
             “Shadowing": 0.5,
             “Soiling": 2.8,
             “Vegetation": 0.2
         }
     }
     ```

### Error Handling

The application uses Python's `logging` module for basic error handling. In case of any error or exception, log messages are printed to the console and log files for detailed debugging. 

#### Design Patterns and Principles

The application follows the following design patterns and principles:

* **Model-View-Controller (MVC):** Although the application does not explicitly separate API endpoints (Controller), business logic (Model) and user interface (View), the organization of the code is inspired by the MVC pattern.
* **Principle of Single Responsibility:** Each function has a specific and single purpose, which makes the code easier to read and maintain.

#### Conclusion

This FastAPI application offers a simple and effective way to deploy machine learning models for PV panel anomaly detection. The user-friendly API endpoint allows developers to easily integrate it into larger systems or applications.

Translated with DeepL.com (free version)
