''' QUESTION=
Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.

array123([1, 1, 2, 3, 1]) → True
array123([1, 1, 2, 4, 1]) → False
array123([1, 1, 2, 1, 2, 3]) → True
'''

array=[1,2,5,6,1,2,3,4,8,9]
def array_123(a):
    for i in range(len(a)):
        if a[i]==1 and a[i+1]==2 and a[i+2]==3:
            return True
    return False
print(array_123(array))