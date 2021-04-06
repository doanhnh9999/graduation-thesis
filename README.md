# Khóa luận tốt nghiệp

1. Cài đặt
2. Chuẩn bị dữ liệu
3. Huấn luyện mô hình
4. Dự đoán

[<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSoHkRzGNSt8Zo7TL1DiYN6QaVEc-Y-etwfEZFRroCvlrWva7U5MSafmg34_I3i9sKLeGk&usqp=CAU">](http://google.com.au/)

## 1. Cài đặt
- Install python 3.7
- Install anaconda
- Install keras, tensorflow
- Install Flask, Ngrok, Fasttext VNCoreNLP

## 2. Chuẩn bị dữ liệu
- Dataset: input, output.
- Input: CharEmbedding (CharRNN).
- Output: WordEmbedding (WordRNN).
- Sentence Format: Every sentense -  (the longest number of words in the sentence, the longest number of characters in the word, number of characters possible). 
- For other sentences, if the length is not large enough, insert a padding character.
- Example: dataset(20, 11, 13, 137): 20 sentenses, each sentence has 11 words, each word has 13 characters, each character is one representing 137 characters.