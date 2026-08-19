import pandas as pd


def detect_amount_anomalies(df: pd.DataFrame) -> pd.DataFrame:
    q1 = df["amount"].quantile(0.25)
    q3 = df["amount"].quantile(0.75)

    iqr = q3 - q1
    upper_threshold = q3 + 1.5 * iqr

    return df[df["amount"] > upper_threshold]


if __name__ == "__main__":
    df = pd.read_csv("data/transactions.csv")

    anomalies = detect_amount_anomalies(df)

    print(anomalies)