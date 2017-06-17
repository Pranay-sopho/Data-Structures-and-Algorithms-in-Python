def insertion_sort(A):
    for j in range(1, len(A)):
        k = j
        while k > 0 and A[k - 1] > A[k]:
            A[k], A[k - 1] = A[k - 1], A[k]
            k -= 1

data = [3, 2, 1, 3, 6,8,1]
insertion_sort(data)
print(data)