words = input().split()
lowercase_words = []

for word in words:
    lowercase = f"{word.lower()}"
    lowercase_words.append(lowercase)

unique = list(set(lowercase_words))

print("Number of unique words:",len(unique))

wordcount = []
for word in unique:
    wordcount.append([len(word),word])

wordcount = sorted(wordcount)

print("Length of the longest word:",wordcount[-1][0])
