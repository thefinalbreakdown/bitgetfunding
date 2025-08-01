
# Bitget Funding Rate History Viewer

A simple Streamlit app to fetch and export historical funding rates from Bitget.

## Features

- Dropdown menu with all Bitget USDT-perp symbols
- Fetch historical funding rate data
- Export results to CSV
- Paginated fetching via cursor

## Run locally

```bash
pip install -r requirements.txt
streamlit run bitget_funding_app.py
```

## Deploy on Streamlit Cloud

1. Fork this repo
2. Go to https://streamlit.io/cloud
3. Deploy the `bitget_funding_app.py`
