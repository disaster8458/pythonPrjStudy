from wordcloud import WordCloud, STOPWORDS
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import re
import pandas as pd
from matplotlib import font_manager, rc
from konlpy.tag import Okt
from collections import Counter

path = 'data/BMDOHYEON_ttf.ttf'
font_name = font_manager.FontProperties(fname=path).get_name()
rc('font', family=font_name)

df = pd.read_csv('data/맛집 유튜브 댓글.csv', encoding='utf-8')
data = list(df['댓글'])

# print(data)
text = ''.join(data)
text = re.compile('[^가-힣 ]').sub('',text)

okt = Okt()

noun_list = okt.nouns(text)
for t1, t2 in enumerate(noun_list) :
    if len(t2) < 2 :
        noun_list.pop(t1)

count = Counter(noun_list)
count_result = count.most_common(50)

ddata = dict(count_result)
plt.figure(figsize=(12,6))
plt.plot(list(ddata.keys())[0:10], list(ddata.values())[0:10])
plt.show()
#
stopwords = set(STOPWORDS)
stopwords.add('said')
wc = WordCloud(font_path='data/BMDOHYEON_ttf.ttf',background_color='white', max_words=2000, stopwords=stopwords)

wc = wc.generate_from_frequencies(dict(count_result))
wc.to_file('맛집.jpg')

plt.figure(figsize=(12,6))
plt.imshow(wc,interpolation='bilinear')
plt.axis('off')
plt.show()