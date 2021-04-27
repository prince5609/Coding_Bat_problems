''' QUESTION=
Given an array of ints, return the number of 9's in the array.

array_count9([1, 2, 9]) → 1
array_count9([1, 9, 9]) → 2
array_count9([1, 9, 9, 3, 9]) → 3
'''
''' METHOD 1--
array=[9,9,9,9,9,8,8,5,5,9,4,4]
def count9(n):
    ans=n.count(9)
    return ans
print(count9(array))
'''

# METHOD 2--
array=[9,9,9,9,5,5,4,4,4,4,4,6,6,6,6,9,9,9]
ans=0
for i in range(len(array)):
    if array[i]==9:
        ans=ans+1
print(ans)