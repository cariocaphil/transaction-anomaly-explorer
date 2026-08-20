import pandas as pd
import pytest

from transaction_anomaly_explorer.validation import validate_transactions


def test_valid_transactions():
    df = pd.DataFrame(
        {
            "transaction_id": [1],
            "customer_id": [101],
            "amount": [50.0],
            "country": ["DE"],
            "merchant_category": ["retail"],
        }
    )

    validate_transactions(df)


def test_missing_required_column():
    df = pd.DataFrame(
        {
            "transaction_id": [1],
            "customer_id": [101],
            "amount": [50.0],
            "country": ["DE"],
        }
    )

    with pytest.raises(ValueError, match="merchant_category"):
        validate_transactions(df)


def test_empty_dataset():
    df = pd.DataFrame(
        columns=[
            "transaction_id",
            "customer_id",
            "amount",
            "country",
            "merchant_category",
        ]
    )

    with pytest.raises(ValueError, match="no transaction rows"):
        validate_transactions(df)