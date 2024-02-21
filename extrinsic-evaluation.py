import random
import re
from collections import defaultdict

import codecs
# Read the text file
file_path = '/content/GPAC.txt'

# Read the corpus from the text file with explicit encoding
with codecs.open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()
import re



def splitData(text, train_ratio=0.8):
  # Split the preprocessed text into words using Amharic punctuation marks as separators
  words = re.split('[።፥፤፦]+', text)

  # Determine the index to split the data
  split_index = int(len(words) * train_ratio)

  # Split the data into training and testing sets
  train_data = words[:split_index]

  test_data = words[split_index:]
  return train_data, test_data
train_data , test_data = splitData(text)
s,e,step = 4,0,-1
d = {2:"trigrams",4:"unigrams",
3:"bigrams",1:"fourgrams"}
train_data = ' '.join(train_data)



def train_ngram_model(text, n):
    ngram_model = defaultdict(list)
    words = text.split()


    for i in range(len(words) - n):
        context = tuple(words[i:i+n])
        target_word = words[i+n]
        ngram_model[context].append(target_word)

    return ngram_model



def next_word_prediction(context, ngram_model):
    if context not in ngram_model:
        return None

    possible_words = ngram_model[context]
    word_counts = defaultdict(int)
    for word in possible_words:
        word_counts[word] += 1

    total_count = sum(word_counts.values())
    probabilities = {word: count / total_count for word, count in word_counts.items()}

    predicted_word = max(probabilities, key=probabilities.get)
    return predicted_word




def evaluate_next_word_prediction(test_data, ngram_model, n):
    sentences = test_data.split('።')
    total_predictions = 0
    correct_predictions = 0

    for sentence in sentences:
        words = sentence.split()
        for i in range(len(words) - n):  # Adjusted loop range
            context = tuple(words[i:i+n])
            target_word = words[i+n]
            predicted_word = next_word_prediction(context, ngram_model)
            if predicted_word == target_word:
                correct_predictions += 1
            total_predictions += 1

    accuracy = correct_predictions / total_predictions
    return accuracy
predict_test = ' '.join(test_data)
for n in range(s,e,step):
#predict_test = ' '.join(test_data)



  #In order to check the accuracy
  #start predicting for different n values
  ngram_model = train_ngram_model(train_data, n)
  accuracy = evaluate_next_word_prediction(predict_test, ngram_model, n)
  print(f"{d[n]} accuracy is: {accuracy}")
