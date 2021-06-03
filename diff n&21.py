"""  QUESTION=
Given an int n, return the absolute difference between n and 21
except return double the absolute difference if n is over 21.
"""


def diff_21(n):
    if n <= 21:
        diff = (21 - n)
        return diff
    else:
        diff = (n - 21) * 2
        return diff


print(diff_21(float(input("ENTER THE VALUE OF N :"))))
