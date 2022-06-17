import string
import pandas as pd
import nltk
from textblob import TextBlob
from easynmt import EasyNMT

data = pd.read_csv("https://raw.githubusercontent.com/Aytureulgen/Tez/main/AppleAirPods2.csv")

reviews = list(data["Column 3"])

model = EasyNMT("opus-mt")

translations = model.translate(reviews, source_lang="tr", target_lang="en")

pos_rev = 0
neg_rev = 0
neu_rev = 0

for trans in translations:

    blob = TextBlob(trans)
    rev_sentiment = blob.polarity
    print("Yoruma ait kutupluluk değeri: ",rev_sentiment)
    print("Yorum", end=" ")
    if rev_sentiment > 0 :
        print("Pozitif")
        pos_rev = pos_rev + 1
    elif rev_sentiment < 0 :
        print("Negatif")
        neg_rev = neg_rev + 1
    else :
        print("Nötr")
        neu_rev = neu_rev + 1

print("Pozitif Yorum Sayısı:", pos_rev)
print("Negatif Yorum Sayısı:", neg_rev)
print("Nötr Yorum Sayısı:", neu_rev)