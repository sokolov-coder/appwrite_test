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

    print("BODY:", context.req.body_text)

    if context.req.body_text:
        request = json.loads(
            context.req.body_text
        )
    else:
        request = {}


    text = request.get(
        "text",
        ""
    )


    result = analyze_text(text)


    return context.res.json(result)