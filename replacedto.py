import csv
import json
import sys
import string


from time import time

with open ("t8.shakespeare.txt",'r') as file:
    filedata = file.read()

a=[]
b=[]

c = time()
with open("french_dictionary.csv") as csvfile:
    ader = csv.reader(csvfile)
    for row in ader:
        a.append(row[0])
        b.append(row[1])
        filedata = filedata.replace(row[0],row[1])


with open("t8.shakespeare.txt",'w') as file:
    file.write(filedata)


translator = str.maketrans('', '', string.punctuation)


word_count = {}
text = open('t8.shakespeare.txt').read()

words = text.split()
for word in words:
    word = word.translate(translator).lower()
    count = word_count.get(word, 0)
    count += 1
    word_count[word] = count

word_count_list = sorted(word_count, key=word_count.get, reverse=True)
for word in word_count_list[:10]:
    print(word, word_count[word])

output_file = open('words2.csv', 'w')
writer = csv.writer(output_file)
writer.writerow(['word', 'count'])
for word in word_count_list:
    writer.writerow([word, word_count[word]])



print("time taken",time()-c)
print("memory",sys.getsizeof(filedata))