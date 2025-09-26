characters = list(map(str, input()))

pairs = []

for j in range(len(characters)):
    for i in range(j,len(characters)):
        if ord(characters[j])<ord(characters[i]):
            pairs.append([characters[j],characters[i]])

print(pairs)
print(len(pairs))
