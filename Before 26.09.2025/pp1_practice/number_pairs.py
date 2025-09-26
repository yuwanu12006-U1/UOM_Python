numbers = list(map(int, input().split(',')))

pairs = []
for i in range(len(numbers)-1):
    if numbers[i] < numbers [i+1]:
        pairs.append([numbers[i],numbers[i+1]])

print(pairs)
print(len(pairs))
