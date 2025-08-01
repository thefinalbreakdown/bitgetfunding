
import streamlit as st
import pandas as pd
import requests
from datetime import datetime

st.title("📈 Bitget Funding Rate History")

@st.cache_data(show_spinner=False)
def get_available_symbols():
    url = "https://api.bitget.com/api/v2/mix/market/tickers?productType=USDT-FUTURES"
    try:
        res = requests.get(url, timeout=10)
        res.raise_for_status()
        data = res.json().get("data", [])
        return sorted([item["symbol"].replace("_", "") for item in data])
    except Exception as e:
        st.error(f"Failed to load symbols from Bitget API: {e}")
        return []

available_symbols = get_available_symbols()

if not available_symbols:
    st.warning("Could not load symbol list from Bitget. Using fallback list.")
    available_symbols = ["BTCUSDT", "ETHUSDT", "SOLUSDT", "XRPUSDT"]

symbol = st.selectbox("Select a symbol", available_symbols)
limit = st.slider("Records per page", min_value=10, max_value=100, value=100)
run = st.button("Fetch Funding Rates")

@st.cache_data(show_spinner=False)
def fetch_funding_rates(symbol, limit=100):
    url = "https://api.bitget.com/api/v2/mix/market/history-fund-rate"
    all_data = []
    page = 1

    while True:
        params = {
            "symbol": symbol,
            "productType": "USDT-FUTURES",
            "pageNo": page,
            "pageSize": limit
        }
        res = requests.get(url, params=params)
        if res.status_code != 200:
            st.error("API Error: " + res.text)
            break

        data = res.json().get("data", [])
        if not data:
            break

        all_data.extend(data)
        if len(data) < limit:
            break
        page += 1

    if not all_data:
        return pd.DataFrame()

    df = pd.DataFrame(all_data)
    if "fundingTime" not in df.columns or "fundingRate" not in df.columns:
        return pd.DataFrame()

    df["fundingTime"] = pd.to_datetime(df["fundingTime"].astype(float), unit='ms')
    df["fundingRate"] = df["fundingRate"].astype(float) * 100
    df = df.rename(columns={"fundingTime": "Time", "fundingRate": "Funding Rate (%)"})
    return df

if run:
    with st.spinner("Fetching funding rate data..."):
        df = fetch_funding_rates(symbol, limit)
        if not df.empty:
            st.success(f"Fetched {len(df)} entries.")
            st.dataframe(df)
            csv = df.to_csv(index=False).encode("utf-8")
            st.download_button("📥 Download CSV", data=csv, file_name=f"{symbol}_funding_rate.csv")
        else:
            st.warning("No data found.")
