import json


def analyze_text(text: str):

    positive = [
        "love",
        "good",
        "great",
        "awesome",
        "happy"
    ]

    negative = [
        "bad",
        "hate",
        "sad",
        "error"
    ]

    score = 0

    lower = text.lower()

    for word in positive:
        if word in lower:
            score += 1

    for word in negative:
        if word in lower:
            score -= 1

    if score > 0:
        sentiment = "positive"
    elif score < 0:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    return {
        "status": "ok",
        "length": len(text),
        "words": len(text.split()),
        "sentiment": sentiment
    }



def main(context):

    context.log(
        f"body={context.req.body}"
    )

    context.log(
        f"body_text={context.req.body_text}"
    )


    text = ""


    # вариант 1: HTTP body
    if context.req.body_text:
        try:
            data = json.loads(
                context.req.body_text
            )
            text = data.get("text", "")
        except Exception:
            pass


    # вариант 2: Appwrite execution data
    if not text and context.req.body:
        try:
            data = json.loads(
                context.req.body
            )
            text = data.get("text", "")
        except Exception:
            pass


    return context.res.json(
        analyze_text(text)
    )