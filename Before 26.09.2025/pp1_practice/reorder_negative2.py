numbers = []
for num in input().split():
    numbers.append(int(num))

for number in numbers:
    if number >= 0:
        print(number, end=" ")

for number in numbers:
    if number < 0:
        print(number, end=" ")
