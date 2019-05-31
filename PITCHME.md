## MacData Summer School Day 5: Introduction to Text Mining
#### Yang Tang, PhD 
@snap[center span-40]
![](assets/img/bagofwords.png)
@snapend
@snap[midpoint span-70]
![](assets/img/wordcloud.pdf)
@snapend

---
#### What is text mining?
@ul

- Text mining (also called text analytics) is a method for finding patterns from a large body text. 
- It is a method for gathering structured information from unstructured data. 
- Typical text mining tasks includes
  - Text categorization
  - Entity extraction,
  - Sentiment analysis
  - Topic identification
  - Document summarization
  
- Essentially, we would like to turn text into data for analysis via natural language processing (NLP) and analytical methods.

@ulend

---
#### High-Level Classification of Text Analytics and Tools Avaiable

![](assets/img/intro_chart.png)

---?image=assets/img/trans_api.png&size=80% 70%
#### A Sneak Peak of Language Detection/Translation API
---?image=assets/img/entities.png&size=60% 80%
#### A Sneak Peak of Natual Language API
---?image=assets/img/sentiment.png&size=50% 80%
#### A Sneak Peak of Natual Language API
---?image=assets/img/catgories.png&size=80% 30%
#### A Sneak Peak of Natual Language API
---
#### Introduction to regular expressions in Python
- What exactly are regular expressions?
- Strings with a special syntax
- Allow us to match patterns in other strings
- Applications of regular expressions:
  - Find all web links in a document
  - Parse email addresses, remove/replace unwanted characters

---?gist=yanggicane/d4767e2c951e32a8fc48ce43c858c7d0&lang=python&title=Textcode
@[1]()
@[3-4](match..)
@[6](match)
@[8-9](match)
---
@snap[north-west]
Common Regex patterns
@snapend
<table>
  <tr>
    <th>pattern</th>
    <th>matches</th>
     <th>example</th>
  </tr>
  <tr>
    <td>`\w+`</td>
    <td>word</td>
     <td>'Magic'</td>
  </tr>
  <tr class="fragment">
    <td>`\d`</td>
    <td>digit</td>
     <td>9</td>
  </tr>
  <tr class="fragment">
    <td>`\s`</td>
    <td>space</td>
     <td>' '</td>
   </tr>
  <tr class="fragment">
    <td>`.*`</td>
    <td>wildcard</td>
     <td>'username74'</td>
    </tr>
  <tr class="fragment">
    <td>`+` or `*`</td>
    <td>greedy match</td>
     <td>'bbbbb'</td> 
  </tr>
  <tr class="fragment">
    <td>`\S`</td>
    <td>**not** space</td>
     <td>'no_spaces'</td> 
  </tr>
  <tr class="fragment">
    <td>`[a-z]`</td>
    <td>lowercase group</td>
     <td>'abcdefg'</td>     
</table>
---
#### Common Python re functions
- split: split a string on regex
- findall: find all patterns in a string
- search: search for a pattern
- match: match an entire string or substring based on a pattern
- Pattern first, and the string second
- The output can be an iterator, string, or match object

---?gist=yanggicane/c7bf46b64f37b90933858f48ee593701&lang=python&title=Textcode
@[1](The sample twitter write into Python as a string.)
@[3-9](We split the sample twitter on each sentence ending.)
@[11-13](Find and print all capitalized words in the sample twitter.)
@[15-17](Split the sample twitter on spaces.)
@[19-21](Find all digits in the sample twitter.)

---
#### The process flow for text data modelling 
![](assets/img/textworkflow.png)

---
#### Example: Movie Information from Rotten Tomatoes
- This dataset consists of general information about 1560 movies on the Rotten Tomatoes site. 
- There are 12 columns: id, synopsis, rating, genre, director, writer, theater_data, dvd_date, currency, box_office, runtime, and studio.
- We are interested in analyzing the movie synopsis. 
- This dataset is avaiable at Kaggle.com.

![span-120](assets/img/movie_data.png)

---?gist=yanggicane/6e8eca98efc75b2ab6902f573dbe97f4
@[1-3](Let's load the movie information from the csv.)
@[5](We will only use the movie discription here.)
@[7](We then delete missing synopsis.)
@[9-12](Let's use one of the movie synopsis as a example for pre-processing.)
@[14-16](Switch to lower case.)
@[18-20](Remove numbers.)
@[22-24](Load standard punctuations.)
@[26-30](Remove punctuations.)

--- 

#### Tokenization
- The next step is to turn a tring or document into tokens (smaller chunks).
- Here, we will break out by words.
- It will help us to remove unwanted tokens (words).
<br/><br/>

#### Remove Stop Words
- In NLP, a stop word is a commonly used word (such as "the", "a", "in") which have very little meaning.
<br/><br/>


#### Stemming
- The goal of stemming is to reduce inflectional forms and sometimes derivationally related forms of a word to a common base form. For example:
  - am, are, is $\rightarrow$ be
  - car, cars, car's cars' $\rightarrow$ car

---?gist=yanggicane/f71fd0b31e91ce624deb44611719b9f1&lang=python&title=CODE
@[1](Import the function to perform word tokenization.)
@[2-49](Return a list of words from the sample text input.)
@[51-52](Define a set of stopwords.)
@[54-83]()
@[85-86]()
@[88-116](Story$\rightarrow$ stori.)

---?gist=yanggicane/e6e12c59e3d5970ebabdf4af358a6394&lang=python&title=NOW LET'S APPLY THE PRE-PROCESSING STEPS TO THE ENTIRE DATASET
@[1-10]()
@[13-15](Convert a collection of text documents to a matrix of token counts.)
@[16-18](Return a dtm with 1498 rows, and 15863 columns (words).)
@[20-26](Compare to the result without stemming.)

---
#### Charting word frequency
- The matplotlib is used by many open source Python projects.
- Straightforward functionality with lots of options.
  @ul
  - Histograms
  - Bar charts
  - Line charts
  - Scatter plots
  - and also advanced functionality like 3D graphs and animations!
  @ulend

---
#### PLOTTING A HISTOGRAM WITH MATPLOTLIB
```Python
from matplotlib import pyplot as plt
plt.hist([1,5,5,7,7,7,9])
plt.show()
```
![fragment](assets/img/hist_eg.png)

---
#### Charting word frequency
```Python
wordsum=dtm_stem.sum(axis=0)
wordsum=wordsum.sort_values(ascending=False)
plt.figure(figsize=(15,10))
plt.bar(wordsum.index.values[0:25], wordsum[0:25])
plt.xlabel("Word")
plt.ylabel("Counts")
plt.show()    
```
---
#### Charting word frequency
![fragment](assets/img/wordfreq.png)

---
#### Generating WordClouds in Python
- Many times you might have seen a cloud filled with lots of words in different sizes.
- The sizes in a wordcloud represent the frequency or the importance of each word.
- Let's see a simple example for generate wordcloud in python. 

```Python 
from wordcloud import WordCloud
sample=movie_synopsis_nomissing[5]
wordcloud = WordCloud().generate(sample)

# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
```
---
#### Generating WordClouds in Python
![fragment](assets/img/wordcloud1.png)


```Python
wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(sample)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
```
---
#### Generating WordClouds in Python
![fragment](assets/img/wordcloud2.png)

---
#### Generating a WordClouds for the Movie DataSet
```Python
joint_synopsis=' '.join(map(str,final_synopsis))
movie_wordcloud=WordCloud(max_font_size=50, max_words=150,background_color="white").generate(joint_synopsis)

plt.figure(figsize=(15,10))
plt.imshow(movie_wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

```
---
![fragment](assets/img/moviewordcloud.png)



--- 
#### Topic Models 
- A topic model takes a collection of unlabelled documents and attempts to find the structure or topics in the collection. 
- It is a great way to automatically explore and structure a large set of documents. 
- As documents on similar topics tend to use a similar sub-vocabulary, the resulting clusters of documents can be interpreted as discussing different 'topics'.
- Latent Dirichlet Allocation (LDA) is an example of a probabilistic topic model. 
- LDA starts from a bag-of-words (dtm) description to represent the different documents.
---
#### LDA model
- An LDA model is defined by two parameters:
  - $\alpha$ A prior estimate on topic probability (average frequency that each topic within a givein document occurs)
  - $\beta$ A collection of $k$ topics where each topic is givein a probability distribution over the vocabulary used in a document corpus.
- For each word in a document:
  - Choose a topic $z\sim$Multinomial ($\theta$)
  - Choose the corresponding topic-word distribution $\beta_z$
  - Draw a word $w\sim$ Multinomial ($\beta_z$)
- When training the model, the goal is to find parameters $\alpha$ and $\beta$, which maximize the probability that the text corpus is generated by the model. 

---?gist=yanggicane/ae333641ef6ffa749630c352d4e97341&lang=python&title=LDA IN PYTHON
@[1]()
@[3-10]()
@[13-31]()
@[33-41]()
@[44-59]()
@[61-83]()
@[85-107]()
@[109-131]()
@[133-155]()
@[157-179]()

---
#### Introduction to API

- API stands for Application Programming Interface.
- It allow applications to communicate with one another.
- There are a lot of publicly available web-based API that returns data, likely JSON, or XML.
- It is the code that governs the access point(s) for the server.
- What can we do with web based APIs?
  - We can send an API a request detailing the information we want.
  - APIs allow us to alter data on other applications, too. 
---

 #### Introduction to JSON
 - JSON stands for JavaScript Object Notation and is basically a way of presenting data. 
 ```JSON
 “restaurant”: {
 “name”: “Fish Witch”,
 “address”: “214 NE Broadway”,
 “zipcode”: “97232”,
 “phone”: “503–000–0000”,
 “website”: “http://fishwitch.com",
 “email”: “hellofishy@fishwitch.com”
}
 ```
 
 
 

