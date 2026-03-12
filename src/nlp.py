from transformers import pipeline
from langdetect import detect
from deep_translator import GoogleTranslator

classifier = pipeline(
    "sentiment-analysis",
    model="cardiffnlp/twitter-roberta-base-sentiment"
    )

def sentimentToNum(text):
    if text[0]["label"] == "LABEL_1":
        return text[0]["score"]
    else:
        return -text[0]["score"]
    
def sentimentCalc(videos):

    result = []

    for video in videos:

        title = checkAndTranslate(video["title"])
        description = checkAndTranslate(video["description"])
        captions = video["captions"]

        titleScore = sentimentToNum(classifier(title))
        descriptionScore = sentimentToNum(classifier(description))

        if captions == 0:
            captionScore = 0
        else:
            captions = checkAndTranslate(captions)
            captionScore = sentimentToNum(
                classifier(captions, truncation=True, max_length=512)
            )

        result.append({
            "video_id": video["video_id"],
            "title_score": titleScore,
            "description_score": descriptionScore,
            "caption_score": captionScore
        })

    return result

def weightedSentiment(scores, titleWeight, descWeight, captionWeight):
    result = []

    for video in scores:

        score = (
            titleWeight * video["title_score"]
            + descWeight * video["description_score"]
            + captionWeight * video["caption_score"]
        )

        result.append(score)

    return result

def proportionSentiments(li):
    positive = 0
    for i in li:
        if i > 0: 
            positive += 1
    return positive/len(li)

def meanSentiments(li):
    return sum(i for i in li)/len(li)

def checkAndTranslate(text):
    MAX_CHARS = 600

    text = text[:MAX_CHARS]

    lang = detect(text)
    if lang != "en":
        text = GoogleTranslator(source = 'auto', target = "en").translate(text)
    return text