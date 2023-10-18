import random, time
import seaborn as sns
import matplotlib.pyplot as plt
from simplex import SimplexSolver

# set the seed for the random number generator to 42 so that we replicate the same results
random.seed(42)

def grow_A(A, grow_to_m, grow_to_n):
    # mutate base matrix to be m x n
    m = grow_to_m - len(A)
    n = grow_to_n - len(A[0])
    if n > 0:
        for i in range(m):
            row = A[i]
            for j in range(n):
                row.append(random.randint(-10, 10))
            A.append(row)
    
    return A

def grow_b(b, grow_to):
    # mutate vector b to be m x 1
    m = grow_to - len(b)
    for i in range(m):
        b.append(random.randint(-10, 10))
    
    return b

def grow_c(c, grow_to):
    # mutate vector c to be n x 1
    n = grow_to - len(c) 
    for i in range(n):
        c.append(1)
    
    return c

# base data pulled from slides
def base_data():
    A = [[1,2,-1,-1], [-1,-5,2,3]]
    b = [1,1]
    c = [1,1,1,1]

    return A, b, c

def simplex(A, b, c, m, n):
    # run simplex
    suffix = "_m" + str(m) + "_n" + str(n)
    start_time = time.time()
    SimplexSolver().run_simplex(A, b, c, prob="min", enable_msg=False, latex=False, suffix=suffix)
    end_time = time.time()
    
    duration = end_time - start_time
    key = f"m_{m} n_{n}"
    stats[key] = duration
    print(f"Execution time for m = {m} and n = {n}:", duration, "seconds")

# m from 2 to 6 to 10 to 14. (in increments of 4)
# n from 4 to 10 ... 50. (in increments of 10)

# prime the base data
A, b, c = base_data()

stats = {}
# for loop for m from 2 to 14 in increments of 4
for m in range(2, 15, 4):
    # for ever m we need to run the simplex for 4 variables 
    # before jumping to 10 and incrementing by 10 up to 50
    # as per the instructions
    simplex(A, b, c, m, 4)

    # for loop for n from 4 to 50 in increments of 10
    for n in range(10, 51, 10):
        # grow the data
        A = grow_A(A, m, n)
        b = grow_b(b, m)
        c = grow_c(c, n)
    
        simplex(A, b, c, m, n)

# set the style of the plot
sns.set_theme(style="whitegrid")

# create a new figure with a specified size
plt.figure(figsize=(10, 10))

# set the title, x-axis label, and y-axis label for the plot
plt.title("Execution Time for Simplex Algorithm")
plt.xlabel("Matrix Size")
plt.ylabel("Execution Time (seconds)")
plt.xticks(rotation=90)

# create a bar plot using the stats dictionary
sns.barplot(x=list(stats.keys()), y=list(stats.values()))

# save the plot to a file and display it
plt.savefig("execution_time.png")