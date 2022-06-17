import string
import pandas as pd
import nltk
from nltk.corpus import stopwords
from matplotlib import pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator

data = pd.read_csv("https://raw.githubusercontent.com/Aytureulgen/Tez/main/AppleAirPods2.csv")

def preprocess_data(data):
    data = data.drop('URL', axis=1)
    data = data.drop('Name', axis=1)

    data['Column 3'] = data['Column 3'].str.strip().str.lower()

    return data

data = preprocess_data(data)

reviews = list(data["Column 3"])

stop_words = stopwords.words('turkish')
stop_words.extend(
    ["bir", "kadar", "sonra", "kere", "mi", "ye", "te", "ta", "nun", "daki", "nın", "ten", "bi", "den", "a"])


def list_to_string(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1


rev = list_to_string(reviews)
word_cloud = WordCloud(width=2000, height=1000, random_state=1,
                       background_color='White', stopwords= stop_words, collocations=False).generate(rev)

plt.imshow(word_cloud)
plt.axis("off")
plt.show()
