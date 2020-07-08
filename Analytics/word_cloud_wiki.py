
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 22 05:23:42 2020
@author: deepak
"""


import wikipedia
#creating a function to get desired data from wikipedia

def get_wiki(query):
    title=wikipedia.search(query)[0]
    page=wikipedia.page(title)
    return page.content

print(get_wiki('data analysis'))

from wordcloud import WordCloud, STOPWORDS

stopword=set(STOPWORDS)

wc=WordCloud(width=800, height=800,
             background_color='White',
             mask=None,
             max_words=200,
             stopwords=stopword,
             min_font_size=10).generate(get_wiki('data analysis'))
             

wc.to_file('wc.png')
