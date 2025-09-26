user = list(map(int, input().split()))

nums =[]
num = 1111
while num < 1111 + user[0]:
    numar = str(num)
    numbar = list(numar)
    for digit in numbar:
        divisors = []
        if int(digit) != 0:
            divisors.append(int(digit))
            print(divisors)
            divisors.remove(1)
            for divisor in divisors:
                if user[0] % divisor == 0:
                    nums.append(num)

    num += 1

print(nums)
