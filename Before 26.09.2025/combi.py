def combinations(alist):
    if len(alist) == 0:
        return [[]]
    sublist = []
    for c in combinations(alist[1:]):
        sublist = sublist + [c,c+[alist[0]]]
    return sublist

print(combinations([1,2,3]))
