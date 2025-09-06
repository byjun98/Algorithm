arr = input()
al = ['c=','c-','dz=','d-','lj','nj','s=','z=']
for i in al:
    arr = arr.replace(i, '*')   # 반환값을 다시 arr에 할당
print(len(arr))  # 몇 개의 알파벳으로 이루어져 있는지 출력
