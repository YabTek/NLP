import nltk
from nltk.util import ngrams
from collections import Counter
import math
import string


nltk.download('punkt')


def preprocess_text(text):
    cleaned_text = text.replace('\n', ' ').replace('\r', '')
    cleaned_text = cleaned_text.translate(str.maketrans('', '', string.punctuation))
    return cleaned_text


def train_language_model(train_data, n, k):
    tokens = nltk.word_tokenize(train_data)
    ngrams_list = list(ngrams(tokens, n))
    ngrams_freq = Counter(ngrams_list)


    model = {}
    for ngram, count in ngrams_freq.items():
        context = tuple(ngram[:-1])
        word = ngram[-1]
        if context not in model:
            model[context] = {}
        model[context][word] = math.log((count + k) / (ngrams_freq[context] + k * len(ngrams_freq)))


    return model


def calculate_perplexity(model, test_data):
    test_tokens = nltk.word_tokenize(test_data)
    num_words = len(test_tokens)
    log_prob_sum = 0.0


    for i in range(len(test_tokens)):
        if i < n-1:
            context = tuple(test_tokens[:i])
        else:
            context = tuple(test_tokens[i-n+1:i])
        word = test_tokens[i]


        if context in model and word in model[context]:
            log_prob = model[context][word]
            log_prob_sum += log_prob


    perplexity = math.exp(-log_prob_sum / num_words)


    return perplexity


with open('/content/GPAC.txt', 'r', encoding='utf-8', errors='ignore') as file:
    text = file.read()


train_size = int(0.8 * len(text))
train_data = text[:train_size]
test_data = text[train_size:]


train_data = preprocess_text(train_data)
test_data = preprocess_text(test_data)


n_values = [1, 2, 3, 4]
k = 0.1  


for n in n_values:
    model = train_language_model(train_data, n, k)
    perplexity = calculate_perplexity(model, test_data)

    print(f"Perplexity for n={n}: {perplexity}")