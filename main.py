import json
import requests


def get_session():
    session = requests.Session()

    session.headers.update({
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/116.0.0.0 Safari/537.36"
        ),
        "Accept": "application/json, text/javascript, */*; q=0.01",
    })

    session.cookies.set(
        "cookiePrivacyPreferenceBannerProduction",
        "notApplicable",
        domain=".tradingview.com",
    )

    session.cookies.set(
        "cookiesSettings",
        '{"analytics":true,"advertising":true}',
        domain=".tradingview.com",
    )

    session.cookies.set(
        "device_t",
        "ZDJIWEJnOjA.FzlbqZZZDUn3rAZsUnCck0IeeBQdNHWNGufTK9Sfq0g",
        domain=".tradingview.com",
    )

    session.cookies.set(
        "sessionid",
        "...",
        domain=".tradingview.com",
    )

    session.cookies.set(
        "sessionid_sign",
        "...",
        domain=".tradingview.com",
    )

    session.cookies.set(
        "tv_ecuid",
        "...",
        domain=".tradingview.com",
    )

    return session

def get_ideas(ticker: str, limit: int = 5):

    session = get_session()

    url = (
        f"https://ru.tradingview.com/"
        f"symbols/{ticker}/ideas/?component-data-only=1"
    )

    headers = {
        "referer": (
            f"https://ru.tradingview.com/"
            f"symbols/{ticker}/ideas/?sort=recent"
        ),
        "x-requested-with": "XMLHttpRequest",
        "x-language": "ru",
    }

    response = session.get(
        url,
        headers=headers,
        timeout=20,
    )

    response.raise_for_status()

    data = response.json()

    return (
        data.get("data", {})
            .get("ideas", {})
            .get("data", {})
            .get("items", [])[:limit]
    )

def main(context):

    request = json.loads(context.req.body_text)

    ticker = request.get("ticker", "IVAT")

    ideas = get_ideas(ticker)

    return context.res.json({
        "ticker": ticker,
        "count": len(ideas),
        "ideas": ideas,
    })