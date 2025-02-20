import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

def train_model():
    df = pd.read_csv("data/fuel_prices.csv")
    df["date"] = pd.to_datetime(df["date"]).map(pd.Timestamp.toordinal)  # Convert date to numeric
    X = df[["date"]]
    y = df["fuel_rate"]
    
    model = LinearRegression()
    model.fit(X, y)
    
    joblib.dump(model, "models/fuel_model.pkl")
    print("Model trained and saved.")

if __name__ == "__main__":
    train_model()
