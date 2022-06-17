from typing import List
import numpy as np
from matplotlib import pyplot as plt

d_freq = {"ürün": 471, "apple": 185, "ses": 224, "şarj": 188, "iyi": 161, "amazon": 167, "kalite": 203,
          "hız": 192, "kargo": 160, "nesil": 125, "olarak": 95, "yok": 112, "güzel": 123, "aldım": 101,
          "geldi": 96, "elime": 79, "gün": 162, "gayet": 81, "kulaklık": 152, "pod": 96}

freqs = list(d_freq.values())
words = list(d_freq.keys())

y_post= np.arange(len(words))

plt.bar(y_post, freqs,align='center',alpha=0.5)
plt.xticks(y_post,words)
plt.ylabel('Sıklık')
plt.xlabel('Kelimeler')
plt.title('En Çok Kullanılan 20 Kelimeye Ait Sıklık Grafiği')
plt.show()
