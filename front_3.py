""" QUESTION=

Given a string, we'll say that the front is the first 3 chars of the string.
If the string length is less than 3, the front is whatever is there. Return a new string which is 3 copies of the front.

front3('Java') → 'JavJavJav'
front3('Chocolate') → 'ChoChoCho'
front3('abc') → 'abcabcabc'
"""
while True:
    def front_3(s):
        if len(s) >= 3:
            front = s[0:3]
            return front + front + front
        elif len(s) < 3:
            front = s
            return front + front + front


    print(front_3(str(input("enter the string :"))))
