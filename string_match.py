''' QUESTION=
Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring.
So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.

string_match('xxcaazz', 'xxbaaz') → 3
string_match('abc', 'abc') → 2
string_match('abc', 'axc') → 0
'''

string1="xxcaazz"
string2="xxbaaz"

def smaller(a,b):
    if len(a)<len(b):
        return a
    else:
        return b
s=smaller(string1,string2)
n=len(s)
def greater(a,b):
    if len(a)>len(b):
        return a
    else:
        return b
g=greater(string1,string2)
num=0
for i in range(n-1):
    if s[i]==g[i] and s[i+1]==g[i+1]:
        num=num+1
print(num)