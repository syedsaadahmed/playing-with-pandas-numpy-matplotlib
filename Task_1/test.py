import collections
import string
import os
import math
import matplotlib.pylab as plt

case_sensitive = False
with open('sample.txt', 'r') as f:
	original_text = f.read()
if case_sensitive:
	alphabet = string.ascii_letters
	text = original_text
else:
	alphabet = string.ascii_lowercase
	text = original_text.lower()
alphabet_set = set(alphabet)
counts = dict(collections.Counter(c for c in text if c in alphabet_set))
# for letter in alphabet:
# 	print(letter, counts[letter])

#print("total:", sum(counts.values()))
my_dict = {}
for key, value in sorted(counts.items(), key=lambda item: item[1], reverse=True):
    my_dict.update({key:value})

#print(my_dict)

# n = math.floor(len(my_dict.items())*0.2)
# for i in range(1,n):
# 	del list(my_dict)[i]
# print('hello')



lists = sorted(my_dict.items()) # sorted by key, return a list of tuples

x, y = zip(*lists) # unpack a list of pairs into two tuples

plt.bar(x, y)
plt.show()



# infile=open('sample.txt', 'r')
# lines=0
# words=0
# characters=0
# for line in infile:
#     line = line.strip(os.linesep)
#     wordslist=line.split()
#     lines=lines+1
#     words=words+len(wordslist)
#     characters=characters+ len(line)
# print(lines)
# print(words)
# print(characters)




