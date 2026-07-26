import json

from src.service.tradingview import get_ideas


def main(context):

    request = json.loads(context.req.body_text)

    ticker = request.get("ticker", "IVAT")

    ideas = get_ideas(ticker)

    return context.res.json({
        "ticker": ticker,
        "count": len(ideas),
        "ideas": ideas,
    })