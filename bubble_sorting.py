# Bubble Sorting
# O(N^2)

a = [8, 5, -7, 0, 10, 1]
N = len(a)

for i in range(0, N - 1):
    for j in range(0, N - 1 - i):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

print(a)
# a = [-7, 0, 1, 5, 8, 10]
