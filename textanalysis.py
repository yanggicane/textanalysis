#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 23 10:52:03 2019

@author: YTang
"""

import re

re.match('abc', 'abcdef')
re.match('abc', 'fedabc')
re.search('abc', 'fedabc')

word_regex='\w+'
re.match(word_regex, 'hi there!')

my_string="Let's write RegEx!"
re.findall(r"\w+", my_string)



sample_twitter="Which moment was your favorite? Asking your friend to come see Pokémon Detective Pikachu with you again for a 3rd time."

sentence_endings = r"[.,?]"
splitthereviewbysentence=re.split(sentence_endings, sample_twitter)
splitthereviewbysentence



capitalized_words = r"[A-Z]\w+"
print(re.findall(capitalized_words, sample_twitter))

# Split my_string on spaces and print the result
spaces = r"\s+"
print(re.split(spaces, sample_twitter))

# Find all digits in my_string and print the result
digits = r"\d+"
re.findall(digits, sample_twitter)



from pandas import DataFrame
import pandas as pd
df = DataFrame.from_csv("movie_info.csv", sep=",")


movie_synopsis=df['synopsis']


####First Step is delete missing values in the review column
movie_synopsis_nomissing=[r for r in movie_synopsis if pd.notnull(r)]


####Let use one of the reviews as example   
sample=movie_synopsis_nomissing[1494]   
sample

###Transfer to lower cases     
sample=sample.lower()        
sample        

###Removing numbers
sample=re.sub(r'\d+', '',sample)
sample        

###Removing punctuation(s)
from string import punctuation
punctuation

#Function to strip punctuation
def strip_punctuation(s):
    return ''.join(c for c in s if c not in punctuation)

sample=strip_punctuation(sample)

sample

####Tokenize
import nltk
nltk.download('punkt')
nltk.download('stopwords')

from nltk.tokenize import word_tokenize
tokenized_words=word_tokenize(sample) ##return a list of 44 words
tokenized_words

####Remove stop words
from nltk.corpus import stopwords 
stop_words = set(stopwords.words('english'))

tokenized_words=[word for word in tokenized_words if word not in stop_words]
tokenized_words

###reduced to 27

###Stemming
from nltk.stem.snowball import SnowballStemmer

stemmer=SnowballStemmer("english",ignore_stopwords=True)
tokenized_words=[stemmer.stem(word) for word in tokenized_words]

tokenized_words


final_synopsis=[]
for r in range(len(movie_synopsis_nomissing)):
    input_document=movie_synopsis_nomissing[r].lower()
    input_document=re.sub(r'\d+','', input_document)
    input_document=strip_punctuation(input_document)
    input_words=word_tokenize(input_document)
    input_words=[word for word in input_words if word not in stop_words]
    input_words=[stemmer.stem(word) for word in input_words]
    clean_synopsis=' '.join(map(str, input_words))
    final_synopsis.append(clean_synopsis)

from sklearn.feature_extraction.text import CountVectorizer    
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(final_synopsis)
dtm_stem=pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names())
dtm_stem.shape   
    
from nltk.tokenize import RegexpTokenizer
token = RegexpTokenizer(r'[a-zA-Z]+')
vectorizer = CountVectorizer(lowercase=True,stop_words='english',ngram_range = (1,1),tokenizer = token.tokenize)
X = vectorizer.fit_transform(movie_synopsis_nomissing)
dtm=pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names())
dtm.shape        

from matplotlib import pyplot as plt
plt.hist([1,5,5,7,7,7,9])
plt.show()

wordsum=dtm_stem.sum(axis=0)
wordsum=wordsum.sort_values(ascending=False)
plt.figure(figsize=(15,10))
plt.bar(wordsum.index.values[0:25], wordsum[0:25])
plt.xlabel("Word")
plt.ylabel("Counts")
plt.show()    



from wordcloud import WordCloud
sample=movie_synopsis_nomissing[5]
wordcloud = WordCloud().generate(sample)

# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(sample)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()



joint_synopsis=' '.join(map(str,final_synopsis))
movie_wordcloud=WordCloud(max_font_size=50, max_words=150,background_color="white").generate(joint_synopsis)

plt.figure(figsize=(15,10))
plt.imshow(movie_wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()


###Topic Models
from sklearn.decomposition import LatentDirichletAllocation

lda_model = LatentDirichletAllocation(n_components=5,               # Number of topics
                                      max_iter=10,               # Max learning iterations
                                      learning_method='online',   
                                      random_state=100,          # Random state
                                      batch_size=128,            # n docs in each learning iter
                                      evaluate_every = -1,       # compute perplexity every n iters, default: Don't
                                      n_jobs = -1,               # Use all available CPUs
                                     )


lda_output = lda_model.fit_transform(dtm_stem)

print(lda_model)  # Model attributes


# Log Likelyhood: Higher the better
print("Log Likelihood: ", lda_model.score(dtm_stem))

# Perplexity: Lower the better. Perplexity = exp(-1. * log-likelihood per word)
print("Perplexity: ", lda_model.perplexity(dtm_stem))


# Show top n keywords for each topic
import numpy as np

def show_topics(lda_model=lda_model, n_words=20):
    keywords = np.asarray(list(dtm_stem))
    topic_keywords = []
    for topic_weights in lda_model.components_:
        top_keyword_locs = (-topic_weights).argsort()[:n_words]
        topic_keywords.append(keywords.take(top_keyword_locs))
    return topic_keywords

topic_keywords = show_topics(lda_model=lda_model, n_words=20)        

# Topic - Keywords Dataframe
df_topic_keywords = pd.DataFrame(topic_keywords)
df_topic_keywords.columns = ['Word '+str(i) for i in range(df_topic_keywords.shape[1])]
df_topic_keywords.index = ['Topic '+str(i) for i in range(df_topic_keywords.shape[0])]

df_topic_keywords


df_topic_keywords.iloc[0]
df_topic_keywords.iloc[1]
df_topic_keywords.iloc[2]
df_topic_keywords.iloc[3]
df_topic_keywords.iloc[4]







        
        