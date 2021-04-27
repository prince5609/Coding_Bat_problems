''' QUESTION=
Given an array of ints, return True if one of the first 4 elements in the array is a 9.
The array length may be less than 4.

array_front9([1, 2, 9, 3, 4]) → True
array_front9([1, 2, 3, 4, 9]) → False
array_front9([1, 2, 3, 4, 5]) → False
'''

array=[]
ans=0
n=int(input("enter how many elements are their in your array :"))
for i in range(n):
    a=int(input("enter your elements now :"))
    array.append(a)
if n>=4:
    for i in range(4):
        if array[i]==9:
            ans=ans+1
    print(ans)
elif n<4:
    for i in range(n):
        if array[i]==9:
            ans=ans+1
    print(ans)
