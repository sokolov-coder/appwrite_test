import json
import os


def analyze_text(text: str):
    positive_words = [
        "love",
        "good",
        "great",
        "awesome",
        "happy"
    ]

    negative_words = [
        "bad",
        "hate",
        "sad",
        "error"
    ]

    lower = text.lower()

    score = 0

    for word in positive_words:
        if word in lower:
            score += 1

    for word in negative_words:
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

    request = json.loads(
        context.req.body
    )

    text = request.get(
        "text",
        ""
    )


    result = analyze_text(text)


    return context.res.json(result)