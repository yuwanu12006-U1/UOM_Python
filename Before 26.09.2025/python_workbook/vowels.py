letter = input().lower()
vowels = 'aeiou'

if letter == 'y':
    print('Sometimes y is a vowel, and sometimes y is a consonant')

elif letter in vowels:
    print('Entered letter is a vowel')

else:
    print('letter is a consonant')
