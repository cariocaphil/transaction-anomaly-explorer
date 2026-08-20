import pandas as pd
from sklearn.ensemble import IsolationForest


def detect_amount_anomalies(df: pd.DataFrame) -> pd.DataFrame:
    q1 = df["amount"].quantile(0.25)
    q3 = df["amount"].quantile(0.75)

    iqr = q3 - q1
    upper_threshold = q3 + 1.5 * iqr

    return df[df["amount"] > upper_threshold]


def detect_ml_anomalies(
    df: pd.DataFrame,
    contamination: float = 0.06,
) -> pd.DataFrame:
    model = IsolationForest(
        contamination=contamination,
        random_state=42,
    )

    predictions = model.fit_predict(df[["amount"]])

    return df[predictions == -1]