import logging
from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import joblib
import pandas as pd

app = FastAPI()

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define the input data structure using Pydantic
class HouseData(BaseModel):
    longitude: float
    latitude: float
    housing_median_age: float
    total_rooms: float
    total_bedrooms: float
    population: float
    households: float
    median_income: float

# Load the pre-trained model (ensure this path is correct)
try:
    model = joblib.load("best_rf_model.pkl")  # Ensure this path is correct
    logger.info(f"Model loaded successfully: {type(model)}")
except Exception as e:
    logger.error(f"Error loading model: {e}")
    model = None

@app.post("/predict")
def predict_price(data: HouseData):
    if model is None:
        logger.error("Model not loaded properly")
        return {"error": "Model not loaded"}

    # Log received data
    logger.info(f"Received data: {data}")

    try:
        # Create input data array for prediction
        input_data = np.array([[ 
            data.longitude,
            data.latitude,
            data.housing_median_age,
            data.total_rooms,
            data.total_bedrooms,
            data.population,
            data.households,
            data.median_income
        ]])

        # Feature engineering for the input data (same as during model training)
        rooms_per_household = input_data[:, 3] / input_data[:, 6]  # total_rooms / households
        bedrooms_per_room = input_data[:, 4] / input_data[:, 3]  # total_bedrooms / total_rooms
        population_per_household = input_data[:, 5] / input_data[:, 6]  # population / households

        # Add the feature-engineered columns to the input data (add them to the right of the original columns)
        input_data = np.hstack((
            input_data,  # original features
            rooms_per_household.reshape(-1, 1),  # rooms_per_household
            bedrooms_per_room.reshape(-1, 1),  # bedrooms_per_room
            population_per_household.reshape(-1, 1),  # population_per_household
            np.zeros((input_data.shape[0], 6))  # Add 6 dummy features for one-hot encoding (set to 0)
        ))

        # Log the transformed input data
        logger.info(f"Transformed input data for prediction: {input_data}")

        # Define column names to match the training features (add all 15 features)
        columns = [
            "longitude", "latitude", "housing_median_age", "total_rooms", "total_bedrooms", 
            "population", "households", "median_income", "category_1", "category_2", "category_3", 
            "category_4", "category_5", "category_6", "rooms_per_household", "bedrooms_per_room", "population_per_household"
        ]

        # Convert to DataFrame with the correct column names
        input_df = pd.DataFrame(input_data, columns=columns)

        # Make the prediction using the loaded model
        predicted_price = model.predict(input_df)[0]

        # Log the predicted price
        logger.info(f"Predicted price: {predicted_price}")

        return {"predicted_price": predicted_price}
    except Exception as e:
        logger.error(f"Error during prediction: {e}")
        return {"error": "Prediction failed", "details": str(e)}
