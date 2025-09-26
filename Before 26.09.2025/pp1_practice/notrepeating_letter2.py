letters = list(map(str, input()))

active = True

for letter in letters:
    letter_count = 0
    while letter in letters:
        letter_count += 1
        letters.remove(letter)
    
    if letter_count == 1:
        active = False
        print(letter)
        break
    
if active:
    print(-1)
