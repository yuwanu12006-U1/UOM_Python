records = []
for _ in range(int(input())):
    details = []
    name = input()
    score = float(input())
    details.append(score)
    details.append(name)
    
    records.append(details)

records.sort()

same_score = []
same_score.append(records[0][1])

for n in range(len(records)-1):
    if records[0][0] == records[n+1][0]:
        same_score.append(records[n+1][1])
     

print(same_score)

for name in same_score:
    print(name)
