word = input()
vowels = 'aeiouAEIOU'

letters = []
for i in range(len(word)):
    if word[i] not in vowels:
        letters.append(word[i])

for letter in letters:
    print(letter, end='')
