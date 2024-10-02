
def Traverser(x, y):
    A = [[1 for _ in range(x)] for _ in range(y)]

    for i in range(1, y):
        for j in range(1, x):
            A[i][j] = A[i - 1][j] + A[i][j - 1]
    
    return A[-1][-1]

print(Traverser(2,3))





