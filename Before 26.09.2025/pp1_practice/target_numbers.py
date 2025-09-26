nums = input().split()
target = int(input())

pairs = []

for _ in nums:
    current_number = int(nums.pop(0))
    for number in nums:
        if int(number) + current_number == target:
            pair = (current_number, int(number))
            pairs.append(pair)

if pairs == []:
    print("None")
else:
    for pair in pairs:
        print(pair)
