#1.4 Generate random sentences using n-grams; explain what happens as n increases, based on your output.

#import ngrams created in question 1.1
from Question1_1 import unigrams,bigrams,trigrams,four_grams

import random

def generate_sentence(ngrams, n, length=10):
    sentence = []

    # Randomly choose a starting n-gram
    current_ngram = random.choice(ngrams[n])

    # Add the words from the starting n-gram to the sentence
    sentence.extend(current_ngram)

    # Generate the rest of the sentence
    for _ in range(length - n):
        # Use the last (n-1) words as the context
        context = tuple(sentence[-(n-1):])

        # Get the next word based on the context
        next_words = [gram[-1] for gram in ngrams[n] if gram[:-1] == context]
        next_word = random.choice(next_words) if next_words else None

        # Add the next word to the sentence
        if next_word:
            sentence.append(next_word)
        else:
            break  # Break if no next word is found based on the context

    return ' '.join(sentence)

# Sample print for generating sentences with different values of n
ngrams = {1: unigrams, 2: bigrams, 3: trigrams, 4: four_grams}
for n_value in range(1, 5):
    generated_sentence = generate_sentence(ngrams, n_value)
    print(f"Generated sentence with n={n_value}:", generated_sentence)

"""
sample prints
Generated sentence with n=1: ሀገር ክፍለ ከቤተሰቦቹ ያው ተሳታፊ እንዲያውም በዚህ ብቅ ቀረጥ ሥራ
Generated sentence with n=2: ከበላህም ይብላህ አለኝ ለብዙ ጊዜ እሠራለሁ እያሉ የያዙትን ነገር ካየህማ
Generated sentence with n=3: ደፍረው ማየትን እንመኛለን ምንም ዓይነት ነፍጥ እንዳያልፍ በአስመራም በኩል ጥብቅ
Generated sentence with n=4: ዓለም ነው ትዳር መመስረት የተጣሉ ባልና ሚስትን የማስታረቅ ያህል ቀላል
"""

"""From the output we can conclude, as the value of n increases, we will get a more meaningful and contextually coherent sentence."""