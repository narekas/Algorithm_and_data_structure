# Algorithm sort inserts
# O(N^2)

a = [8, 5, -7, 0, 10, 1]
N = len(a)

for i in range(1, N):
    for j in range(i, 0, -1):
        if a[j] < a[j - 1]:
            a[j], a[j - 1] = a[j - 1], a[j]
        else:
            break

print(a)
# a = [-7, 0, 1, 5, 8, 10]
