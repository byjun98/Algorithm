L, C = map(int, input().split())     # L: 암호 길이, C: 문자 개수
arr = list(input().split())          # 사용할 문자들 입력
arr.sort()                           # 사전순 정렬 (출력도 사전순이 되도록)

vowels = ['a', 'e', 'i', 'o', 'u']   # 모음 리스트
path = []                            # 현재까지 선택한 문자들을 담는 배열

def dfs(start, depth):
    # depth : 현재까지 고른 문자의 개수
    # start : 다음에 선택할 수 있는 문자의 시작 인덱스
    
    # 1. 길이가 L이 되었을 때 조건 확인
    if depth == L:
        vowel_count = 0   # 모음 개수
        consonant_count = 0  # 자음 개수

        # path 안의 문자들을 하나씩 검사
        for ch in path:
            if ch in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

        # 조건: 모음 1개 이상, 자음 2개 이상
        if vowel_count >= 1 and consonant_count >= 2:
            # 리스트를 문자열로 합쳐 출력
            print(''.join(path))
        return

    # 2. 아직 길이가 L이 안 됐다면 다음 문자 선택
    for i in range(start, C):
        path.append(arr[i])           # 문자 선택
        dfs(i + 1, depth + 1)         # 다음 재귀 호출 (다음 문자부터 선택)
        path.pop()                    # 선택 해제 (백트래킹)

# DFS 시작: 처음에는 0번 인덱스부터, 길이는 0
dfs(0, 0)
