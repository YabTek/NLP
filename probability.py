#1.3 What is the probability of the sentence. "ኢትዮጵያ ታሪካዊ ሀገር ናት ". You can also try more sentences.

#import the necessary libraries
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
from nltk import FreqDist

#import ngrams created in question 1.1
from Question1_1 import unigrams,bigrams,trigrams,four_grams


#define the given sentence
sentence = "ኢትዮጵያ ታሪካዊ ሀገር ናት"

# Tokenize the sentence
words = word_tokenize(sentence)

# Calculate the probabilities using interpolation
def calculate(words, ngrams):
    # Set interpolation weights
    lambdas = [0.4, 0.3, 0.2, 0.1]

    # Initialize probability
    probability = 1.0

    # Loop through each token in the sentence
    for i in range(len(words)):
        # Get the n-gram context
        context = words[0:i+1]

        # Check if the n-gram context exists in the n-grams
        if tuple(context) in ngrams[i]:

            # Calculate the conditional probability using the n-gram
            conditional_probability = ngrams[i][tuple(context)] / sum(ngrams[i].values())

            # Update the overall probability using interpolation
            probability *= (lambdas[i] * conditional_probability)

    return probability

# define list of frequency distributions of the large corpus for the four ngrams
freqDistList = [FreqDist(unigrams), FreqDist(bigrams), FreqDist(trigrams), FreqDist(four_grams)]


print(f"The interpolated probability of the sentence '{sentence}' is: {calculate(words, freqDistList)}")


"""
sample print
The interpolated probability of the sentence 'ኢትዮጵያ ታሪካዊ ሀገር ናት' is: 6.819281351280151e-11

"""