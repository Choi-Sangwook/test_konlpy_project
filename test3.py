# test3.py
# data/sample2.csv 파일에서 명사를 추출한 뒤 빈도수를 계산하고 워드클라우드를 생성합니다.

import csv

import matplotlib.pyplot as plt
from konlpy.tag import Okt
from wordcloud import WordCloud


okt = Okt()
lines = []
word_dic = {}

# CSV 파일 읽기
with open("./data/sample2.csv", encoding="cp949", newline="") as raws:
    reader = csv.reader(raws)
    for row in reader:
        lines.append(row)

# CSV 한 줄을 문자열로 합친 뒤 형태소 분석
for line in lines:
    text = " ".join(line)
    mal_list = okt.pos(text, norm=True, stem=True)

    # 명사만 추출해서 빈도 계산
    for word, tag in mal_list:
        if tag == "Noun":
            word_dic[word] = word_dic.get(word, 0) + 1

# 빈도순 정렬 후 상위 50개 출력
key = sorted(word_dic.items(), key=lambda x: x[1], reverse=True)
for word, count in key[:50]:
    print(f"{word}: {count}")

# 워드클라우드 생성 및 저장
# wordcloud = WordCloud(
#     font_path="./font/malgunsl.ttf",
#     background_color="white",
#     width=1000,
#     height=800,
# ).generate_from_frequencies(word_dic)
#
# plt.figure(figsize=(10, 10))
# plt.imshow(wordcloud)
# plt.axis("off")
# plt.show()

# wordcloud 모양을 원하는 도형 모양으로 변경하기
# mask 옵션 사용함
from PIL import Image   # 이미지 파일 열기용 클래스
import numpy as np  # 배열 다루는 모듈


img = Image.open("./images/heart.png")
imgArray = np.array(img)    # 이미지의 각 픽셀을 숫자 배열로 변환함

wordcloud = WordCloud(
    font_path="./font/malgunsl.ttf",
    background_color="white",
    width=1000,
    height=800,
    max_font_size=100,  # 빈도수가 가장 큰 글자의 크기 지정
    mask=imgArray,  # 사용하고자 하는 이미지의 수치 배열
)
wordcloud.generate_from_frequencies(word_dic)
plt.figure(figsize=(10, 10))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()