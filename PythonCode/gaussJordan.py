import numpy as np
def gauss_jordan(A, b):
    """
    Solves the system of linear equations Ax = b using the Gauss-Jordan method.
    
    Parameters:
    A (list of lists): The coefficient matrix (n x n).
    b (list): The right-hand side vector (n).
    
    Returns:
    list: The solution vector x (n).
    """
    n = len(A)
    
    # Form the augmented matrix
    aug_matrix = [A[i] + [b[i]] for i in range(n)]
    
    for i in range(n):
        # Find the pivot element
        pivot = aug_matrix[i][i]
        if pivot == 0:
            # Swap with a row below to get a non-zero pivot
            for j in range(i+1, n):
                if aug_matrix[j][i] != 0:
                    aug_matrix[i], aug_matrix[j] = aug_matrix[j], aug_matrix[i]
                    pivot = aug_matrix[i][i]
                    break
        
        # Normalize the pivot row
        for k in range(i, n + 1):
            aug_matrix[i][k] = aug_matrix[i][k] / pivot
        
        # Eliminate the entries in the current column for all other rows
        for j in range(n):
            if j != i:
                factor = aug_matrix[j][i]
                for k in range(i, n + 1):
                    aug_matrix[j][k] = aug_matrix[j][k] - factor * aug_matrix[i][k]

    # Extract the solution from the augmented matrix
    x = [aug_matrix[i][-1] for i in range(n)]
    A_n = np.array(aug_matrix)
    return x, A_n[:,0:3]

# Example usage
if __name__ == "__main__":
    A = [
        [2, 1, -1],
        [-3, -1, 2],
        [-2, 1, 2]
    ]
    b = [8, -11, -3]

    solution,B = gauss_jordan(A, b)
    print(B)
    print(f"Roots: {solution}")
