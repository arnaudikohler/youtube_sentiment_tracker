from transformers import pipeline

classifier = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
    )

def sentimentToNum(text):
    if text["label"] == "POSITIVE":
        return text["SCORE"]
    else:
        return -text["SCORE"]
    
