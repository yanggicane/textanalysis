## Welcome to Day 5 of the Summer School!
#### Introduction to Text Mining
---

#### Introduction to regular expressions
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
#### Word toenization with NLTK
###### What is tokenization?
- Turning a string or a document into *tokens* (smaller pieces).
- One common steop in preparing text for anlaysis. 
- There are many different theories and rules.
- You can create your own rules using regex.
- Some common practice:
  - Breaking out words or sentences
  - Separating punctuation
  - Seperating all hashtags in a tweet
- nltk (natual language toolkit) library is commonly used for tokenization. 

```python
from nltk.tokenize import word_tokenize

word_tokenize("Hello world!")
Out[49]: ['Hello', 'world', '!']
```
---
#### Why tokenize?
- Matching common words
- Removing unwanted tokens
#### Cleaning and preprocessing text
- Common steps for preprocessing text includes:
  - Makes all text lowercase
  - Romoves punctuation like periods and question marks
  - Remove numbers
  - Removes tabs and extra spaces
  - Removes specific words(stop words or/and words defined by user)
  

