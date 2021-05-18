# Naver News Crawler

이 크롤러는 개인적인 학습용으로 만들어졌습니다.

이 크롤러는 네이버API를 이용하여 검색어 기반 네이버 포탈 기사를 크롤링해주는 크롤러입니다.
크롤링할수있는 기사의 양은 네이버API의 한도에 따라서 달라질 수 있습니다.

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FNamsik-Yoon%2FNaverNewsCrawler&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

## 안내
네이버 오픈API의 Client ID 및 Secret을 필요로하며 해당 정보는 https://developers.naver.com/products/datalab/ 에서 발급받을 수 있습니다.
출력값은 관련도 순으로 저장이 되며 해당 파일은 csv형식으로 저장이 됩니다.

## 사용방법
```
git clone https://github.com/Namsik-Yoon/NaverNewsCrawler.git
pip install -r requirements.txt
python NaverNewsCrawler.py
```
