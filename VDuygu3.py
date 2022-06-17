import string
import pandas as pd
import nltk
from easynmt import EasyNMT
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

data = pd.read_csv("https://raw.githubusercontent.com/Aytureulgen/Tez/main/AppleAirPods3.csv")

reviews = list(data["Column 3"])

model = EasyNMT("opus-mt")

translations = model.translate(reviews, source_lang="tr", target_lang="en")

pos_rev = 0
neg_rev = 0
neu_rev = 0

for trans in translations:

    sent_analyzer = SentimentIntensityAnalyzer()

    sentiment_dict = sent_analyzer.polarity_scores(trans)

    print("Yoruma ait özet bilgi : ", sentiment_dict)
    print("Yorum", sentiment_dict['neg']*100, "% Negatif")
    print("Yorum", sentiment_dict['neu']*100, "% Nötr")
    print("Yorum", sentiment_dict['pos']*100, "% Pozitif")
    print("Yorum", end = " ")
    if sentiment_dict['compound'] >= 0.05 :
        print("Pozitif")
        pos_rev = pos_rev +1
    elif sentiment_dict['compound'] <= - 0.05 :
        print("Negatif")
        neg_rev = neg_rev + 1
    else :
        print("Nötr")
        neu_rev = neu_rev + 1

print("Pozitif Yorum Sayısı:", pos_rev)
print("Negatif Yorum Sayısı:", neg_rev)
print("Nötr Yorum Sayısı:", neu_rev)