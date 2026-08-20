import pandas as pd
import streamlit as st
from pandas.errors import ParserError

from transaction_anomaly_explorer.analysis import detect_amount_anomalies
from transaction_anomaly_explorer.validation import validate_transactions


def load_data():
    data_source = st.radio(
        "Data source",
        ["Sample dataset", "Upload CSV"],
    )

    if data_source == "Sample dataset":
        return pd.read_csv("data/transactions.csv")

    uploaded_file = st.file_uploader(
        "Upload transaction CSV",
        type="csv",
    )

    if uploaded_file is None:
        st.info("Upload a CSV file to start the analysis.")
        st.stop()

    try:
        return pd.read_csv(uploaded_file)
    except (ParserError, UnicodeDecodeError, OSError) as exc:
        st.error(f"Could not read CSV: {exc}")
        st.stop()


def show_metrics(df, anomalies):
    total_transactions = len(df)
    anomaly_count = len(anomalies)
    anomaly_rate = anomaly_count / total_transactions * 100

    col1, col2, col3 = st.columns(3)

    col1.metric("Transactions", total_transactions)
    col2.metric("Anomalies", anomaly_count)
    col3.metric("Anomaly rate", f"{anomaly_rate:.1f}%")


def filter_by_country(df):
    countries = ["All"] + sorted(df["country"].unique().tolist())
    selected_country = st.selectbox("Country", countries)

    if selected_country == "All":
        return df

    return df[df["country"] == selected_country]


def main():
    st.title("Transaction Anomaly Explorer")

    df = load_data()

    try:
        validate_transactions(df)
    except ValueError as error:
        st.error(str(error))
        st.stop()

    anomalies = detect_amount_anomalies(df)

    show_metrics(df, anomalies)

    filtered_df = filter_by_country(df)

    filtered_anomalies = anomalies[
        anomalies["transaction_id"].isin(filtered_df["transaction_id"])
    ]

    st.subheader("Transactions")
    st.dataframe(filtered_df)

    st.subheader("Transaction amounts")
    chart_data = filtered_df.set_index("transaction_id")["amount"]
    st.bar_chart(chart_data)

    st.subheader("Detected anomalies")
    st.dataframe(filtered_anomalies)


if __name__ == "__main__":
    main()