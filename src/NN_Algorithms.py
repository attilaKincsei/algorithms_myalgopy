"""  My collection of algorithms sources:
https://en.wikipedia.org/wiki/Algorithm

http://python-textbok.readthedocs.io/en/1.0/Sorting_and_Searching_Algorithms.html

Problem Solving with Algorithms and Data Structures using Python:
http://interactivepython.org/runestone/static/pythonds/index.html

Udemy course: Algorithms and Data Structures in Python:
https://www.udemy.com/algorithms-and-data-structures-in-python/?utm_source=adwords-learn&utm_medium=udemyads&utm_campaign=NEW-AW-PROS-TECH-ROW-DSA-EN-EURO_._ci__._sl_ENG_._vi_TECH_._sd_All_._la_EN_._&utm_content=deal4584&utm_term=_._ag_47581515732_._ad_192487854602_._de_c_._dm__._pl__._ti_dsa-304639795623_._li_9063089_._pd__._&gclid=CjwKCAiA78XTBRBiEiwAGv7EKrTf1CJuqFL15b5qEN3GTiyMsqEH2f_Oh8-iEhvXR88EREy1iG_ecRoCLvAQAvD_BwE

Algorithm Education in Python - short course py2.7
http://legacy.python.org/workshops/2002-02/papers/15/index.htm

Algorithms in Python.md (modified from the excellent: Grokking Algorithms)
https://gist.github.com/Integralist/9763bded76e7d826535a3caeafc3bdff

algorithms module in python:
https://pypi.python.org/pypi/algorithms

books:
/home/akincsei/Documents/___CodeCool/Books/python books/
[Kent_D._Lee,_Steve_Hubbard]_Data_structures_and_algorithms_with_Python.pdf
"""
############ ALGORITHM THEORY ######################

### Tree recursion ########
# Fibonacci sequence is a good example for tree recursion
# Visualizing recursion:
# http://interactivepython.org/runestone/static/pythonds/Recursion/pythondsintro-VisualizingRecursion.html

# Tree recursion in Python:
# One should not conclude from this difference that tree-recursive processes are useless.
# When we consider processes that operate on hierarchically structured data rather than
# numbers, we will find that tree recursion is a natural and powerful tool. Furthermore,
# tree-recursive processes can often be made more efficient, as we will see in Chapter 3.
# http://www.idc-online.com/technical_references/pdfs/information_technology/Tree_Recursion_in_Python.pdf

# Linear recursion and iteration, Tree recursion, Greatest Common Divisor
# https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-11.html#%_sec_1.2.2

### Fibonacci sequences:
# See fibonacci.py: Playing around with Fibonacce sequences
# https://www.codewars.com/trainer/python

## Memoized recursive Fibonacci sequences:
# http://ujihisa.blogspot.hu/2010/11/memoized-recursive-fibonacci-in-python.html

# A slow literal implementation of fibonacci function in Python is like the below:

def fib(n):
    return n if n < 2 else fib(n-2) + fib(n-1)


# This is slow but you can make it faster with memoize technique, reducing the order.

__fib_cache = {}
def fib(n):
    if n in __fib_cache:
        return __fib_cache[n]
    else:
        __fib_cache[n] = n if n < 2 else fib(n-2) + fib(n-1)
        return __fib_cache[n]



####### FOR LOOPS ####################

### 0. Understanding for loops
for i in range(1, 4):
    print(i)
    for j in range(11, 14):
        print(j)


### I. List creation with with for loops

# 1. a1 creates a list of filled with the same 10 elements 4 times
list2 = []
for i in range(4):
    for j in range(1, 11):
        list2.append(j)

print(list2, 'list2')


# 1. a1 creates a list of 4 sublists each with 11 elements
row_matrix = []
matrix1 = []
for j in range(1, 11):
    row_matrix.append(j)
for i in range(4):
    matrix1.append(row_matrix)

# 1. a2 DOES THE SAME: creates a list of 4 sublists each with 11 elements
matrix2 = [[j for j in range(1, 11)] for i in range(4)]

# 1. b1: creates a list with 4 sublists each having 4*11 = 44 elements. WHY????????
row_matrix3 = []
matrix3 = []
for i in range(4):
    for j in range(1, 11):
        row_matrix3.append(j)
        matrix3.append(row_matrix3)


####### NESTED FOR LOOPS

# 1. b1: creates a list with 4 sublists each having 4*11 = 44 elements. WHY????????
# You need to use [:] to add copies of the actual state of the
# sublist at every turn of the nested for loop.
row_matrix4 = []
matrix4 = []
for i in range(4):
    for j in range(1, 11):
        row_matrix4.append(j)
        matrix4.append(row_matrix4[:])


print(matrix1, 'matrix1')
print(matrix2, 'matrix2')
print(matrix3, 'matrix3')
print(matrix4, 'matrix4')



### II. List creation with with nested for loops


## EXTRACTING ELEMENTS from a list into a list with sublists of the same length

list_orig = []
for i in range(4):
    for j in range(1, 11):
        list_orig.append(j)

print(list_orig, 'list_orig')

# produce this:
sublist1 = []
list_target = []

for j in range(1, 11):
    sublist1.append(j)
for i in range(4):
    list_target.append(sublist1)

print(list_target, 'list_target')


# solution1:

list_work = []
ssub_list = []
for i in range(4):
    frst = (i * 10)
    lst = ((i + 1) * 10)
    for j in range(frst, lst):
        ssub_list.append(list_orig[j])
    list_work.append(ssub_list)
    ssub_list = []


print(list_work, 'list_work, sol1')


# solution2 with list comprehension:
list_work2 = [[list_orig[j] for j in range((i * 10), ((i + 1) * 10))] for i in range(4)]

print(list_work2, 'list_work2, sol2')




### MATRIX transposition ########

#!!!!!!!!!!!!!!!!!!! 2B CONTINUED from _Snip4.py




####### QUESTIONS ####################
