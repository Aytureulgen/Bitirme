import string
import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter

data = pd.read_csv("https://raw.githubusercontent.com/Aytureulgen/Tez/main/AppleAirPods2.csv")

def preprocess_data(data):

    data = data.drop('URL', axis=1)
    data = data.drop('Name', axis=1)

    data['Column 3'] = data['Column 3'].str.strip().str.lower()

    return data

data = preprocess_data(data)

reviews = list(data["Column 3"])

stop_words = stopwords.words('turkish')
stop_words.extend(["bir","kadar","sonra","kere","mi","ye","te","ta","nun","daki","nın","ten", "bi", "den", "a"])

def list_to_string(s):

    str1 = ""
    for ele in s:
        str1 += ele
    return str1

rev = list_to_string(reviews)

tokens = nltk.tokenize.word_tokenize(rev, language="turkish")

tokens = [token.lower() for token in tokens if token.isalpha()]

tokens = [token for token in tokens if not token in stop_words]

tokens.sort()

freq_of_words = Counter(tokens)

#print(len(tokens))
#print(len(freq_of_words))

#print(freq_of_words.most_common(20))