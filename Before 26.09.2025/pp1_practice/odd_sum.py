numbers = list(map(int, input().split(',')))
odd_nums = []
for number in numbers:
    if number % 2 != 0:
        odd_nums.append(number)

print(sum(odd_nums))
