# Enter your code here. Read input from STDIN. Print output to STDOUT

num_elements = int(input())
elements = input().split()

l = []
for i in range (0,num_elements):
    l.append(int(elements[i]))

print(l)

t = tuple(l)

h = hash(t)
print(h)
