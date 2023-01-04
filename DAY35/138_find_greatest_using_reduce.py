from functools import reduce

l = [1, 2, 3, 4, 5, 6, 677, 8, 9, 21, 31, 4,  4, 5, 1, 2, 34, 54, 55, 67, 89, 90, 89, 85, 65, 12, 3, 4, 65, 7, 6, 7]

a = reduce(max, l)

print(a)


