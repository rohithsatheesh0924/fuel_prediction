import pandas as pd

def predict_fuel_rate(future_date, df):
    future_date = pd.to_datetime(future_date)  # Convert input to datetime

    # Ensure dataframe has date in datetime format
    df["date"] = pd.to_datetime(df["date"])

    # Check if the date exists in the dataset
    if future_date in df["date"].values:
        return df.loc[df["date"] == future_date, "price"].values[0]  # Return actual price

    # If date is not in dataset, predict based on trend
    df = df.sort_values("date")  # Sort by date

    # Use linear interpolation for missing dates
    df.set_index("date", inplace=True)
    df = df.resample("D").interpolate(method="linear")

    if future_date in df.index:
        return round(df.loc[future_date, "price"], 2)  # Predicted price

    return "Prediction unavailable for the given date."

