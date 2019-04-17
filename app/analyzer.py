from textblob import TextBlob



def get_sentiment(review):
    blob = TextBlob(review)
    return blob.sentiment.polarity