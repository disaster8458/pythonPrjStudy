from wordcloud import WordCloud, STOPWORDS
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

path = 'data/BMDOHYEON_ttf.ttf'
font_name = font_manager.FontProperties(fname=path).get_name()
rc('font', family=font_name)

text = open('data/09. alice.txt').read()
mask = np.array(Image.open('data/09. alice_mask.png'))
stopwords = set(STOPWORDS)
stopwords.add('said')

wc = WordCloud(background_color='white', font_path=path, max_words=2000, stopwords=stopwords, mask=mask)

wc = wc.generate(text)
# wc.to_file('alice.jpg')

plt.figure(figsize=(12,12))
plt.imshow(wc,interpolation='bilinear')
plt.axis('off')
plt.show()