cities = input().split()
distances = list(map(int, input().split()))

distances.insert(0,0)

matrix = []
relative_distance = 0
for i in range(len(cities)):
    relative_distance -= distances[i]
    reference = relative_distance

    row = []
    for distance in distances:
        element = relative_distance + distance
        relative_distance += distance
        row.append(element)

    relative_distance = reference

    print(row)
