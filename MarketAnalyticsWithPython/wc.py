filename = "/home/deepak/python.txt"
mytext = open(filename).read()
print(mytext)




from wordcloud import WordCloud, STOPWORDS

stopword=set(STOPWORDS)

wc=WordCloud(width=1584, height=396,
             background_color='White',
             mask=None,
             max_words=200,
             stopwords=stopword,
             min_font_size=10).generate(mytext)
             

wc.to_file('wc.png')
