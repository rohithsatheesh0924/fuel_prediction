from src.predict import predict_fuel_rate
from data.preprocess import load_and_preprocess_data
import pandas as pd

# Define the path to your CSV file
CSV_FILE_PATH = "data/fuel_prices.csv"

def validate_date(date_str):
    """Validate if the entered date is in the correct format."""
    try:
        pd.to_datetime(date_str, format="%Y-%m-%d")  # Check format
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    df = load_and_preprocess_data(CSV_FILE_PATH)  # Load preprocessed data

    while True:
        future_date = input("Enter a date (YYYY-MM-DD) for prediction: ")
        
        if validate_date(future_date):  
            break  # Exit loop if valid date
        else:
            print("❌ Invalid date format! Please enter in YYYY-MM-DD format.")

    predicted_rate = predict_fuel_rate(future_date, df)  # Call prediction function

    print(f"Predicted fuel rate for {future_date}: ₹{predicted_rate} INR")  # Show in INR
