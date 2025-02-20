import pandas as pd

def load_and_preprocess_data(file_path="data/fuel_prices.csv"):
    df = pd.read_csv(file_path)
    df["date"] = pd.to_datetime(df["date"])  # Convert date to datetime
    df = df.sort_values("date")  # Ensure chronological order
    return df

if __name__ == "__main__":
    df = load_and_preprocess_data()
    print(df.head())
