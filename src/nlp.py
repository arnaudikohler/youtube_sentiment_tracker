from transformers import pipeline

classifier = pipeline(
    "sentiment-analysis",
    model="cardiffnlp/twitter-roberta-base-sentiment"
    )

dic = {'title': 'Non-profitable Trader.😂😭 #memecoin #crypto #bitcoin #meme #pino #solana #trading #business #money', 
       'description': '', 'video_id': 'trVmDXMaj-M'}

tu = classifier(dic["title"])
print(tu)

def sentimentToNum(text):
    if text[0]["label"] == "LABEL_1":
        return text[0]["score"]
    else:
        return -text[0]["score"]
    
def sentimentCalc(dict):
    titleWeight = 0.7
    captionWeight = 0.15
    descriptionWeight = 0.15
    result = []
    for video in dict:
        titleScore = sentimentToNum(classifier(video["title"]))
        descriptionScore = sentimentToNum(classifier(video["description"]))
        captions = video["captions"]
        if captions == 0:
            captionScore = 0
        else:
            captionScore = sentimentToNum(classifier(captions, truncation=True, max_length=512))
        result.append(
            titleWeight * titleScore + descriptionWeight * descriptionScore + captionWeight * captionScore
        )
    
    return result
    
