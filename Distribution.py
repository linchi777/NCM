# -*- coding: utf-8 -*-
from snownlp import SnowNLP
import codecs
import os

source = open('C:\\Users\\Administratior\\Desktop\\ncm\\comments.txt', 'r', encoding='UTF-8')
line = source.readlines()
sentimentslist = []
for i in line:
    s = SnowNLP(i.encode('utf-8').decode('utf-8'))
    print(s.sentiments)
    sentimentslist.append(s.sentiments)

import matplotlib.pyplot as plt
import numpy as np
plt.hist(sentimentslist, bins = np.arange(0, 1, 0.01), facecolor = 'g')
plt.xlabel('Sentiments Probability')
plt.ylabel('Quantity')
plt.title('Analysis of Sentiments')
plt.show()
