import requests

# URL of the API
url = "http://localhost:8000/predict"

# House data (ensure this matches the model input parameters)
payload = {
    "longitude": -122.23,
    "latitude": 37.88,
    "housing_median_age": 41.0,
    "total_rooms": 880.0,
    "total_bedrooms": 129.0,
    "population": 322.0,
    "households": 126.0,
    "median_income": 8.3252
}

# Send POST request to the API with the house data
response = requests.post(url, json=payload)

# Handle and display the prediction result
if response.status_code == 200:
    # If successful, print the predicted house price
    print("Predicted house price:", response.json())
else:
    # If there’s an error, print the error details
    print("Error:", response.text)
