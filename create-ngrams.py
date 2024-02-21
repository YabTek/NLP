#1.1 Create n-grams for n=1, 2, 3, 4. You can show sample prints

#import the common function which is defined in a file common.py
from common import create_ngrams

#call a function and show sample prints
unigrams = create_ngrams(1)
print("Unigrams-->", unigrams[:3])

bigrams = create_ngrams(2)
print("Bigrams-->", bigrams[:3])

trigrams = create_ngrams(3)
print("Trigrams-->", trigrams[:3])

four_grams = create_ngrams(4)
print("Fourgrams-->", four_grams[:3])


"""
sample prints
Unigrams--> [('ምን',), ('መሰላችሁ',), ('አንባቢያን',)]
Bigrams--> [('ምን', 'መሰላችሁ'), ('መሰላችሁ', 'አንባቢያን'), ('አንባቢያን', 'ኢትዮጵያ')]
Trigrams--> [('ምን', 'መሰላችሁ', 'አንባቢያን'), ('መሰላችሁ', 'አንባቢያን', 'ኢትዮጵያ'), ('አንባቢያን', 'ኢትዮጵያ', 'በተደጋጋሚ')]
Fourgrams--> [('ምን', 'መሰላችሁ', 'አንባቢያን', 'ኢትዮጵያ'), ('መሰላችሁ', 'አንባቢያን', 'ኢትዮጵያ', 'በተደጋጋሚ'), ('አንባቢያን', 'ኢትዮጵያ', 'በተደጋጋሚ', 'ጥሪው')]

"""