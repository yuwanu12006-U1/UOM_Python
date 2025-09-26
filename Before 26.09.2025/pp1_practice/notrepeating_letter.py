letters = list(map(str, input()))

for letter in letters:
    count = 0
    while letter in letters:
        letters.remove(letter)
        count += 1

    if count == 1:
        print(letter)
        break

    letters.insert(0,0)
