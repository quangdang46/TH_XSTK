import matplotlib.pyplot as plt
import numpy as np

with open('data.txt', 'r') as f:
  text = f.read()

words = text.split()
freq = {}
for word in words:
  if word in freq:
    freq[word] += 1
  else:
    freq[word] = 1


sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
top_30 = sorted_freq[:30]

words, frequencies = zip(*top_30)

frequencies = np.array(frequencies)

words = np.array(words)


fig = plt.figure(figsize=(7, 7))
plt.bar(words, frequencies)
plt.title('Frequency of the 30 most common words')
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.xticks(rotation=90)
plt.show()





