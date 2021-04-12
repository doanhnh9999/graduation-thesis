from vncorenlp import VnCoreNLP
import numpy as np
import csv
import re
import string
from collections import Counter
import numpy as np
import random

annotator = VnCoreNLP(address="http://127.0.0.1", port=9000)

def split(word):
  return [(word[:i], word[i:]) for i in range(len(word) + 1)]

def delete(word):
  return [l + r[1:] for l,r in split(word) if r]

def pick_word_from_fake(list_word):
    index_chose = random.randint(0, len(list_word) - 1)
    return list_word[index_chose]

input_train = []
with open('../data/CG_address.csv', encoding='utf8') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        input_train.append(row[0].lower())

sentense_corpus = []
for i in input_train:
    sentense_corpus.append(annotator.tokenize(i))

data_train = []
for i in sentense_corpus:
    for j in i:
        data_train.append(j)

sentence_source = []
sentence_destination = []

for i in data_train:
    source = i.copy()
    for j in range(2):
        sentence_source.append(source)
        index_chose = random.randint(0, len(i) - 1)
        word_pick = i[index_chose]
        i[index_chose] = pick_word_from_fake(delete(word_pick))
        sentence_destination.append(i)


# print(len(sentence_source))
# print(sentence_destination)

# sentense_corpus_file = []
# for i in range(len(sentence_source)):
#     for j in range(len(sentence_source[i])):
#         print(sentence_destination[i][j] + " 0 0 " + sentence_source[i][j])
#     print("\n")


train_dataset = open("test_ver2.txt","a",encoding='utf8')
for i in range(len(sentence_source)):
    sentence_token = sentence_destination[i]
    sentence_tag   = sentence_source[i]
    for j in range(len(sentence_token)):
        train_dataset.write(str(sentence_token[j]))
        train_dataset.write(' ')
        train_dataset.write('0')
        train_dataset.write(' ')
        train_dataset.write('0')
        train_dataset.write(' ')
        train_dataset.write(str(sentence_tag[j]))
        train_dataset.write('\n')
    train_dataset.write('\n')
train_dataset.close()
    # len_sen = len(self.tokens)
    # print("{len_sen} sentence".format(len_sen=len_sen))
    # result = result + "\n"
    # sentense_corpus_file.append(result)

# print(sentense_corpus_file)

# fileout = open('sentence_input.txt', 'a+', encoding='utf8')
# np.savetxt(fileout, sentense_corpus_file)
# fileout.close()


#=================Write data_train to file===================
# def write_to_file(source, destination):
#     for i in source:
#         for j in range(len(i) - 1):
            