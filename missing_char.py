'''  QUESTION=
Given a non-empty string and an int n, return a new string where the char at index n has been removed.
The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).

missing_char('kitten', 1) → 'ktten'
missing_char('kitten', 0) → 'itten'
missing_char('kitten', 4) → 'kittn'
'''

def missing_char(s,n):
    while n not in range(len(s)):
        print("you have entered a wrong value of n,try again")
        print(missing_char(str(input("enter the string :")), int(input("enter the value of n :"))))

    if n in range(len(s)):
        new_s=s.replace(s[n],"")
        return new_s
print(missing_char(str(input("enter the string :")),int(input("enter the value of n :"))))

