from fastapi import FastAPI
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from typing import List, Dict

from .stocks import fetch_undervalued_stocks

app = FastAPI()

# cache for stocks
data_cache: List[Dict[str, float]] = []

def update_stocks() -> None:
    global data_cache
    tickers = [
        "AAPL",
        "MSFT",
        "GOOG",
        "AMZN",
        "META",
    ]
    data_cache = fetch_undervalued_stocks(tickers)


scheduler = BackgroundScheduler(timezone="UTC")
scheduler.add_job(update_stocks, CronTrigger(hour=8, minute=0))
scheduler.start()

# run immediately on startup
update_stocks()


@app.get("/undervalued")
def get_stocks() -> List[Dict[str, float]]:
    return data_cache
