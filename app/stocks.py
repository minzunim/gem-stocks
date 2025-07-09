import yfinance as yf
from typing import List, Dict


def fetch_undervalued_stocks(tickers: List[str]) -> List[Dict[str, float]]:
    """Fetch a list of undervalued stocks based on P/E ratio."""
    results = []
    for ticker in tickers:
        try:
            info = yf.Ticker(ticker).info
            pe = info.get("trailingPE")
            if pe is not None and pe < 15:
                results.append({"symbol": ticker, "pe_ratio": pe})
        except Exception:
            # Ignore network or data errors and continue
            continue
    return sorted(results, key=lambda x: x["pe_ratio"])
