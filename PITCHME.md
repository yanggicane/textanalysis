# Welcome to Day 5 of the Summer School!

# Introduction to Text Mining
## Introduction to regular expressions
* What exactly are regular expressions?
* Strings with a special syntax

``` python3

import re

re.match('abc', 'abcdef')
Out[2]: <re.Match object; span=(0, 3), match='abc'>

word_regex='\w+'

word_regex='\w+'

re.match(word_regex, 'hi there!')
Out[4]: <re.Match object; span=(0, 2), match='hi'>

```
---
<!-- page_number: true -->
