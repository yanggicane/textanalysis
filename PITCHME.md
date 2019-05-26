layout : top-left
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
@title[Common Regex patterns]


@snap[north]
Table Data Fragments
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
    <td></td>
    <td>94</td>
  </tr>
  <tr class="fragment">
    <td>John</td>
    <td>43</td>
  </tr>
</table>


