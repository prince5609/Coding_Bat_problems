''' QUESTION=
Given a string, return the count of the number of times that a substring length 2 appears in the string
and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).

last2('hixxhi') → 1
last2('xaxxaxaxx') → 1
last2('axxxaaxx') → 2
'''

string="abcabcabcabcab"
num=0
for i in range(len(string)-2):
    if string[-2]==string[i] and string[-1]==string[i+1]:
        num=num+1
print(num)