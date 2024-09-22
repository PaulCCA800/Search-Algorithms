
def counting_sort(A, n, k):
    B = [0] * (len(A) + 1)
    C = [0] * (k)
    #Init B and C

    for j in range(0, n):
        C[A[j]] = C[A[j]] + 1
    for i in range(0, k):
        if i == 0:
            continue
        else:
            C[i] = C[i] + C[i - 1]
    #Set correct counting values   
  
    for j in range(n - 1, -1, -1):
        B[C[A[j]]] = A[j]
        C[A[j]] = C[A[j]] - 1
    #Copy values and handle duplicates

    del B[0]
    return B
        
D = [3, 7, 8, 0, 2, 6]

print(counting_sort(D, 6, 9))
