import math

def merge(A, p, q, r):
    L = A[p : q + 1]
    R = A[q  + 1 : r + 1]
    
    i = 0
    j = 0
    k = p
    
    while((i < len(L)) and (j < len(R))):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1
        k = k + 1
   
    while i < len(L):
        A[k] = L[i]
        i = i + 1
        k = k + 1
    
    while j < len(R):
        A[k] = R[j]
        j = j + 1
        k = k + 1

def merge_sort(A, p, r):
    if p < r:
        mid = math.floor((p + r)/2)
        merge_sort(A, p, mid)
        merge_sort(A, mid + 1, r)
        merge(A, p, mid, r)

B = [4,3,2]
a = 0
c = 1

merge_sort(B, a, c)
print(B)

