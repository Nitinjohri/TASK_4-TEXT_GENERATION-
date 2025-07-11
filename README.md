COMPANY: CODTECH IT SOLUTIONS
NAME: NITIN JOHRI
INTERN ID: CT06DG1491
DOMAIN: ARTIFICIAL INTELLIGENCE
DURATION: 6 WEEKS
MENTOR: NEELA SANTOSH
I have made a code upon text generation through training a model upon a sample text.In model,i have used embedding layer,dense layers and lstm layers to learn pattern from the sample text.I have listed the step how i created this amazing text generation model and also provided the output for more understanding of individual upon the topic:
1) Text Tokenization:
  The input text is broken into words and each word is assigned a unique number (index).
  For example: "Artificial Intelligence is..." → [1, 2, 3, ...].
2) N-gram Sequence Creation:
 From the text, short word sequences are created using a sliding window.
 Example: "Artificial Intelligence is" → ["Artificial Intelligence", "Artificial Intelligence is"].
 These are the input patterns the model will learn from.
3) Padding:
 Since sequences can be of different lengths, they are padded with zeros to make them equal in size,This is necessary for
 training the neural network.
4) Inputs and Labels:
 The model learns to predict the next word in a sequence.
 Example: Given "Artificial Intelligence", predict "is".
5) One-hot Encoding:
 The target/output words are converted to one-hot encoded vectors (e.g., a vector of 0s and 1s)
6) LSTM Model:
The model uses:
An Embedding layer to convert word indices into dense word vectors,An LSTM layer to learn patterns and dependencies in word sequences.
A Dense layer with softmax to predict the most likely next word,It is trained using categorical cross-entropy loss and the Adam optimizer.
7) Text Generation:
After training, the model can generate text word-by-word,Take a seed phrase (e.g., "Artificial Intelligence"),
Predict the next word,Add that word to the phrase,Repeat this process to build a sentence of desired length.
Outputs:
Artificial Intelligence is transforming industries industries industries industries learn patterns powerful patterns patterns powerful powerful predictions patterns powerful.
