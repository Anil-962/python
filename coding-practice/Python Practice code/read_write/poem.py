# poem.txt contains famous poem "Road not taken" by poet Robert Frost. 
# You have to read this file in your python program and find out words with maximum occurance.


word_stats={ }
with open("poem.txt", "r") as f:
    for line in f:
        words  = line.split(' ')
        for word in words:
            word = word.strip().lower()
            if word in word_stats:
                word_stats[word] += 1
            else:
                   word_stats[word] = 1
print(word_stats)   
 
word_occurence = list(word_stats.values())
max = max(word_occurence)
print("The most occurring word is :",word_occurence)
print("The number of times it occurred is :")
for word, count in word_stats.items():
    if count==max:
        print(word)
