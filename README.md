# Gem Stocks

This project contains a simple FastAPI application that exposes a list of
potentially undervalued stocks. The list is updated every day at 8 AM UTC using
`APScheduler` and basic data from Yahoo Finance via `yfinance`.

## Running the server

Install dependencies and start the application with `uvicorn`:

```bash
pip install poetry
poetry install
poetry shell
poetry run uvicorn app.main:app --reload
```

Access the list at `http://localhost:8000/undervalued`.

Note that fetching stock information requires network access.
