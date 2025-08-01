
# Bitget Funding Rate Viewer (Correct v2 API)

A fully working Streamlit app using the correct v2 Bitget funding rate endpoint with pagination.

## Features

- Live dropdown of Bitget USDT-perp symbols (underscores removed)
- Proper use of v2 funding rate endpoint with pagination
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
