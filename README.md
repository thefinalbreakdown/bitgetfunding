
# Bitget Funding Rate History Viewer (Final Symbol Fix)

Streamlit app to view and export Bitget perpetual funding rate history, with correct symbol format conversion.

## Features

- Live dropdown of all Bitget USDT-futures symbols (underscores removed)
- Safe handling of missing data
- CSV export
- Fully deployable to Streamlit Cloud

## Run locally

```bash
pip install -r requirements.txt
streamlit run bitget_funding_app.py
```

## Deploy on Streamlit Cloud

1. Fork this repo
2. Go to https://streamlit.io/cloud
3. Deploy the `bitget_funding_app.py`
