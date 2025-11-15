import sys
input = sys.stdin.readline

def recursion(s, l, r, counter):
    counter[0] += 1
    
    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        return recursion(s, l+1, r-1, counter)

def isPalindrome(s):
    counter = [0]
    result = recursion(s, 0, len(s)-1, counter)
    return result, counter[0]

T = int(input())
for _ in range(T):
    S = input().strip()
    result, count = isPalindrome(S)
    print(result, count)
