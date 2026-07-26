from session_config import get_session


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