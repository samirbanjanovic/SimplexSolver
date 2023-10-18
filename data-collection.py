import ast
from simplex import SimplexSolver


def run_simplex(Ax, bx, cx):
  A = ast.literal_eval(Ax)
  b = ast.literal_eval(bx)
  c = ast.literal_eval(cx)

  SimplexSolver().run_simplex(A, b, c, prob="min", enable_msg=False, latex=True)
  

# run the solver for default function from sample
Ax = "[[1,2,-1,-1], [-1,-5,2,3]]"
bx = "[1,1]"
cx = "[1,1,1,1]"




run_simplex(Ax, bx, cx)