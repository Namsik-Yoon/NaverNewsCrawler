#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import pandas as pd
try:
    from bs4 import BeautifulSoup
except:
    get_ipython().system('pip install beautifulsoup4')
    from bs4 import BeautifulSoup

class Crawler:
    def __init__(self):
        self.client_id = input('client ID : ')
        self.client_secret = input('client secret : ')
        self.search_word = input('검색 단어 : ')
        self.encode_type = 'json'
        self.max_display = 100
        self.sort = 'sim'

    def crawling(self,n_contents=None):
        if n_contents!=None:
            assert type(n_contents) is int, '정수값이 필요합니다.'
        start = 1
        df = pd.DataFrame(columns=['title','contents','date'])
        while True:
            url = f"https://openapi.naver.com/v1/search/news.{encode_type}?query={search_word}&display={str(max_display)}&start={str(start)}&sort={sort}"
            headers = {'X-Naver-Client-Id' : self.client_id,
               'X-Naver-Client-Secret':self.client_secret
               }
            r = requests.get(url, headers=headers)
            try:links = [x['link'] for x in r.json()['items'] if 'naver' in x['link']]
            except KeyError:break
            for link in links:
                if i%100==0:print(i)
                if n_contents != None:
                    if i==n_contents:
                        break
                try:
                    req = requests.get(link)
                    html_parser = BeautifulSoup(req.content,'html.parser')
                    title = html_parser.select('h3#articleTitle')[0].text
                    contents = html_parser.select('#articleBodyContents')[0].get_text().replace('\n', "")
                    contents = contents.replace("// flash 오류를 우회하기 위한 함수 추가function _flash_removeCallback() {}", "")
                    contents = contents[:contents.find('▶')]
                    df.loc[i] = [title,contents]
                    i+=1
                except IndexError:continue
            start+=1
        self.result = df
    
    def save(self,path=None):
        if path==None:
            self.result.to_csv('result.csv',encoding="cp949")
        else:
            self.result.to_csv(f'{path}/result.csv',encoding="cp949")
    def get_df(self):
        return self.result

