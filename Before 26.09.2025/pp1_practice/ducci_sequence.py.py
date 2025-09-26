numbers = eval(input())

count = 0
while any(x != 0 for x in numbers):
    mod_numbers = []
    for i in range(len(numbers)):
        try:
            number = numbers[i]-numbers[i+1]
            number *= -1 if number < 0 else 1
            mod_numbers.insert(i, number)

        except IndexError:
            number = numbers[i]-numbers[0]
            number *= -1 if number < 0 else 1
            mod_numbers.insert(i, number)

    numbers = mod_numbers.copy()
    count += 1

print(count, "Steps")
