
# Bitget Funding Rate History Viewer (Safe Version)

A simple Streamlit app to fetch and export historical funding rates from Bitget with robust error handling.

## Features

- Dropdown menu with Bitget USDT-futures symbols
- Safe handling of missing funding data
- Export to CSV
- Streamlit Cloud deployable

## Run locally

```bash
pip install -r requirements.txt
streamlit run bitget_funding_app.py
```

## Deploy on Streamlit Cloud

1. Fork this repo
2. Go to https://streamlit.io/cloud
3. Deploy the `bitget_funding_app.py`
