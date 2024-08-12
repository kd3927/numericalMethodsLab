## module gaussElimin
''' x = gaussElimin(a,b).
Solves [a]{b} = {x} by Gauss elimination.
'''
import numpy as np
def gaussElimin(a,b):
    n = len(b)
    # Elimination phase
    for k in range(0,n-1):
        for i in range(k+1,n):
            if a[i,k] != 0.0:
                lam = a [i,k]/a[k,k]
                a[i,k+1:n] = a[i,k+1:n] - lam*a[k,k+1:n]
                b[i] = b[i] - lam*b[k]
    # Back substitution
    for k in range(n-1,-1,-1):
        b[k] = (b[k] - np.dot(a[k,k+1:n],b[k+1:n]))/a[k,k]
    return b

if __name__ == "__main__":
    

    # Enter coefficient matrices
    a = np.array([[4,-2,1],[-2,4,-2],[1,-2,4]],dtype="float")
    b = np.array([11,-16,17],dtype='float')

    # Call the Gauss Elimination method
    gaussElimin(a, b)
    print(b)