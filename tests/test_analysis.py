import pandas as pd

from transaction_anomaly_explorer.analysis import detect_amount_anomalies


def test_detect_amount_anomalies():
    df = pd.DataFrame({
        "amount": [20, 30, 40, 50, 60, 70, 80, 10000]
    })

    result = detect_amount_anomalies(df)

    assert len(result) == 1
    assert result.iloc[0]["amount"] == 10000