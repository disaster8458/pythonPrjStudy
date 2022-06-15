from wordcloud import WordCloud, STOPWORDS
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import pandas as pd
import re

path = 'data/BMDOHYEON_ttf.ttf'
font_name = font_manager.FontProperties(fname=path).get_name()
rc('font', family=font_name)
text = pd.read_csv('data/instargram2.csv')

text2 = ''.join(text['댓글'])
text2 = re.compile('[^가-힣 ]+').sub('', text2).strip()

mask = np.array(Image.open('data/09. heart.jpg'))
stopwords = set(STOPWORDS)
stopwords.add('said')

wc = WordCloud(font_path='data/BMDOHYEON_ttf.ttf',background_color='white', max_words=2000, stopwords=stopwords, mask=mask)

wc = wc.generate(text2)
wc.to_file('아린 댓글 모음.jpg')

plt.figure(figsize=(12,12))
plt.imshow(wc,interpolation='bilinear')
plt.axis('off')
plt.show()