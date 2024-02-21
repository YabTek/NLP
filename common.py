#import the necessary libraries
from nltk.util import ngrams
from nltk.tokenize import word_tokenize

#read the file
corpus = open('GPAC.txt', 'r', encoding='utf-8', errors = 'ignore').read()

#tokenize the text into words
words = word_tokenize(corpus)

#list of possible punctuations in the corpus
punctuations = {'፡', '።', '፣', '፤', '፥', '፦', '፧',  '፤፤', '.' ,'(', ')', '?', '::','!'}

#remove punctuations from the corpus
cleaned_words = []

for word in words:
    if any(char in punctuations for char in word):
        cleaned_word = ''.join(char for char in word if char not in punctuations)
        if cleaned_word:
            cleaned_words.append(cleaned_word)
    else:
        cleaned_words.append(word)


#define a function to create n-grams
def create_ngrams(n):
  ngram = list(ngrams(cleaned_words, n))
  return ngram