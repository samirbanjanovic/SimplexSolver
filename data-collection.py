import random
from simplex import SimplexSolver

# write a function that will receive the number of constraints and number of variables as input
# in the format of m and n respectively
# using the input, generate a random matrix A of size m x n
# generate a random vector b of size m
# generate a random vector c of size n
# keep the numbers between -100 and 100 and name the function as generate_data
# return A, b, c
def generate_A_matrix(m, n):
    # create matrix A that's m x n
    A = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(random.randint(-100, 100))
        A.append(row)
    
    return A

def generate_b_vector(m):
    # create vector b that's m x 1
    b = []
    for i in range(m):
        b.append(random.randint(-100, 100))
    
    return b

def generate_c_vector(n):
    # create vector c that's n x 1
    c = []
    for i in range(n):
        c.append(random.randint(-100, 100))
    
    return c

def generate_data(m, n):
    A = generate_A_matrix(m, n)
    b = generate_b_vector(m)
    c = generate_c_vector(n)

    return A, b, c

def textbook_data():
    A = [[1,2,-1,-1], [-1,-5,2,3]]
    b = [1,1]
    c = [1,1,1,1]

    return A, b, c

m = 2
n = 4

# first solve for textbook data
A, b, c = textbook_data()

solver = SimplexSolver()
solver.run_simplex(A, b, c, prob="min", enable_msg=False, latex=True)

