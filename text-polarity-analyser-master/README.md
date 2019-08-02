# Text polarity analyser

To find the polarity of a text using NLTK. 

### Tech
http://www.nltk.org/

## Requirements

```sh
nltk version 3.0 or above
```

### How to use?
To run code:
```sh
python polarity_analyser.py
```
### File descriptions

```inc``` -  contains words that increases polarity of text. Ex word 'very' - Here 'very good' has more positive polarity than 'good'.

```dec``` - contains words that decreases polarity of text. Ex word 'barely' - Here 'barely good' has less positive polarity than 'good'.

```inv``` - contains inverse words such as 'not'. Ex 'not good' means it is 'bad'.

Add relavent words to above files to increase the accuracy.

```pos``` - contains positive words.
```neg``` - contains neagative words.


### Result
Python script finds polarity as a integer value. 
Text is negative in nature if polarity is negative else text is positive in nature.




