import numpy as np
from keras.models import Sequential
from keras.layers import LSTM,Dense,Embedding
from keras.utils import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
data = """Artificial Intelligence is transforming industries.
Machine Learning allows computers to learn patterns.
Deep Learning uses neural networks for powerful predictions."""
tokenizer = Tokenizer()
tokenizer.fit_on_texts([data])
word_index = tokenizer.word_index
total_words = len(word_index) + 1
input_sequences = []
for line in data.split('.'):
    token_list = tokenizer.texts_to_sequences([line])[0]
    for i in range(1, len(token_list)):
        n_gram = token_list[:i+1]
        input_sequences.append(n_gram)
max_len = max(len(seq) for seq in input_sequences)
input_sequences = pad_sequences(input_sequences, maxlen=max_len, padding='pre')
xs = input_sequences[:, :-1]
ys = input_sequences[:, -1]
ys = np.eye(total_words)[ys]
model = Sequential()
model.add(Embedding(total_words, 10, input_length=max_len-1))
model.add(LSTM(100))
model.add(Dense(total_words, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(xs, ys, epochs=300, verbose=1)
def generate_text(seed, next_words=20):
    for _ in range(next_words):
        token_list = tokenizer.texts_to_sequences([seed])[0]
        token_list = pad_sequences([token_list], maxlen=max_len-1, padding='pre')
        predicted = model.predict(token_list, verbose=0)
        predicted_word = tokenizer.index_word[np.argmax(predicted)]
        seed += " " + predicted_word
    return seed
print(generate_text("Artificial Intelligence"))