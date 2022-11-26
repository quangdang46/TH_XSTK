'''
4. Find the frequency of each word in a given text (at least 300 words), and draw a 
histogram of the frequency of word with parameter bin = 30.
'''

import matplotlib.pyplot as plt
import numpy as np

with open('data.txt', 'r') as f:
  text = f.read()

text = text.lower()
text = text.replace('.','')
text = text.replace(',','')

words = text.split()
words = list(set(words))

freq = [text.count(i) for i in words]

word, frequencies = zip(*sorted(zip(words, freq), key=lambda x: x[1], reverse=True))

frequencies = np.array(frequencies)

word = np.array(word)

fig = plt.figure(figsize=(7, 7))
plt.hist(frequencies, bins=30)
plt.title('Frequency of the most common words')
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.xticks(rotation=90)
plt.show()

# fig = plt.figure(figsize=(7, 7))
# plt.bar(word, frequencies)
# plt.title('Frequency of the most common words')
# plt.xlabel('Words')
# plt.ylabel('Frequency')
# plt.xticks(rotation=90)
# plt.show()



















