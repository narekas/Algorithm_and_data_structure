# Sort select
# O(N^2)

a = [-3, 5, 0, -8, 1, 9]
N = len(a)

for i in range(N - 1):
    m = a[i]
    p = i
    for j in range(i + 1, N):
        if m > a[j]:
            m = a[j]
            p = j

    if p != i:
        t = a[i]
        a[i] = a[p]
        a[p] = t

print(a)
# a = [-8, -3, 0, 1, 5, 9]
