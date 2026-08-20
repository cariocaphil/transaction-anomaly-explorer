import pandas as pd

from transaction_anomaly_explorer.analysis import (
    detect_amount_anomalies,
    detect_ml_anomalies,
)


def test_detect_amount_anomalies():
    df = pd.DataFrame(
        {
            "amount": [20, 30, 40, 50, 60, 70, 80, 10000],
        }
    )

    result = detect_amount_anomalies(df)

    assert len(result) == 1
    assert result.iloc[0]["amount"] == 10000


def test_detect_ml_anomalies():
    df = pd.DataFrame(
        {
            "transaction_id": [
                "T001",
                "T002",
                "T003",
                "T004",
                "T005",
                "T006",
                "T007",
                "T008",
                "T009",
                "T010",
            ],
            "amount": [
                20,
                25,
                30,
                35,
                40,
                45,
                50,
                55,
                60,
                10000,
            ],
        }
    )

    result = detect_ml_anomalies(
        df,
        contamination=0.1,
    )

    assert len(result) == 1
    assert result.iloc[0]["transaction_id"] == "T010"
    assert result.iloc[0]["amount"] == 10000