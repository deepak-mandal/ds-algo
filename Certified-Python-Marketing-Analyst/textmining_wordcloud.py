'''
pip install wikipedia wordcloud
'''


'''
/*To perform text mining*/
pip install nltk
nltk.download()
'''

import wikipedia

#Creating a function to get desired data from wikipedia
def get_wiki(query):
    title = wikipedia.search(query)[0]
    page = wikipedia.page(title)
    return page.content

print (get_wiki("python programming language"))

from wordcloud import WordCloud, STOPWORDS

stopword = set(STOPWORDS)
    
wc = WordCloud(width = 800, height = 800, 
                   background_color="White",
                   mask=None,
                   max_words=200,
                   stopwords=stopword,
                   min_font_size = 10).generate(get_wiki("python programming language"))
   
wc.to_file("word_cloud.png")
    