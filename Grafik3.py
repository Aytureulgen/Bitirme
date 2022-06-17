from typing import List
import numpy as np
from matplotlib import pyplot as plt

d_freq = {"ses": 76, "apple": 54, "iyi": 55, "kalite": 67, "pod": 31, "amazon": 33, "seri": 28,
          "ürün": 65, "olarak": 24, "nesil": 43, "gayet": 21, "hız": 31, "gerçek": 20, "gün": 18,
          "kesin": 20, "yok": 23, "kulaklık": 37, "ettim": 16, "güzel": 17, "sorun": 22}

freqs = list(d_freq.values())
words = list(d_freq.keys())

y_post= np.arange(len(words))

plt.bar(y_post, freqs,align='center',alpha=0.5)
plt.xticks(y_post,words)
plt.ylabel('Sıklık')
plt.xlabel('Kelimeler')
plt.title('En Çok Kullanılan 20 Kelimeye Ait Sıklık Grafiği')
plt.show()