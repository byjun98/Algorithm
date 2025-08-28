S = input()
result = []
for i in range(len(S)):
    if 'a' <= S[i] <= 'z':
        result.append(chr((ord(S[i])-ord('a')+13)%26+ord('a')))
    elif 'A' <= S[i] <= 'Z':
        result.append(chr((ord(S[i])-ord('A')+13)%26+ord('A')))
    else:
        result.append(S[i])
print(''.join(result))