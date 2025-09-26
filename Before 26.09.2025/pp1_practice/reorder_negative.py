numbers = input().split()
non_negative = []
negative = []
reordered_numbers = []
for number in numbers:
    if int(number) < 0:
        negative.append(number)
    else:
        non_negative.append(number)

reordered_numbers.append(non_negative)
reordered_numbers.append(negative)

for i in range(2):
    for j in range(len(reordered_numbers[i])):
        print(reordered_numbers[i][j], end=" ")
