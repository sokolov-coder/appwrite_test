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