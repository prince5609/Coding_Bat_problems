""" QUESTION=

Given a string and a non-negative int n, return a larger string that is n copies of the original string.

string_times('Hi', 2) → 'HiHi'
string_times('Hi', 3) → 'HiHiHi'
string_times('Hi', 1) → 'Hi'
"""
'''
method 1--

def n_copies(s,n):
    copy=(s)*n
    return copy
print(n_copies(str(input("enter the string :")),int(input("enter value of n :"))))
'''


# SECOND METHOD
def n_copy(s, n):
    copy = s
    for i in range(n - 1):
        copy = copy + s
    return copy


print(n_copy(str(input("enter the string :")), int(input("enter value of n :"))))
