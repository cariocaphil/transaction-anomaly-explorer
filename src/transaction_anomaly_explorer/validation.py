REQUIRED_COLUMNS = {
    "transaction_id",
    "customer_id",
    "amount",
    "country",
    "merchant_category",
}


def validate_transactions(df):
    missing_columns = REQUIRED_COLUMNS - set(df.columns)

    if missing_columns:
        raise ValueError(
            "CSV is missing required columns: "
            + ", ".join(sorted(missing_columns))
        )

    if df.empty:
        raise ValueError("CSV contains no transaction rows.")