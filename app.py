import pandas as pd
import streamlit as st

from transaction_anomaly_explorer.analysis import detect_amount_anomalies

st.title("Transaction Anomaly Explorer")

df = pd.read_csv("data/transactions.csv")

st.subheader("Transactions")
st.dataframe(df)

anomalies = detect_amount_anomalies(df)

st.subheader("Detected anomalies")
st.dataframe(anomalies)