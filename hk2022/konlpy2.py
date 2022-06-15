from konlpy.tag import Kkma, Hannanum, Okt

kkma = Kkma()
han = Hannanum()
okt = Okt()
text = '한국어 분석을 시작합니다 재미있어요~~~'

print(kkma.sentences(text))
print(kkma.nouns(text))
print(kkma.pos(text))
print('='*50)
print(han.nouns(text))
print(han.pos(text))
print('='*50)
print(okt.nouns(text))
print(okt.pos(text))