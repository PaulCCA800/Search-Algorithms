def insertion_sort(A, n):
    for i in range(1, n):
        key = A[i]
        j = i - 1
        while (j > 0 and A[j] > key):
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = key




B = [1, 5, 7, 2, 9, 3, 1]
insertion_sort(B, 7)
print(B)


