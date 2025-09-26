n = int(input())
arr = map(int, input().split())
    
scores = set(arr)
print(scores)
scores.remove(max(scores))
print(scores)
print(max(scores))
