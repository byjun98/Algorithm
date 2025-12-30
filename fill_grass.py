import os
import subprocess
import re
import random
from datetime import datetime

# --- 설정: Algorithm 최상위 폴더에 두고 실행하세요 ---

def find_problem_path(root_path, problem_number):
    """
    root_path부터 시작해서 모든 하위 폴더를 뒤져서
    '문제번호.' 으로 시작하는 폴더를 찾습니다.
    """
    print(f"🔍 '{problem_number}'번 문제 폴더를 검색 중...", end="", flush=True)
    
    for dirpath, dirnames, filenames in os.walk(root_path):
        # .git 폴더는 검색 건너뛰기
        if '.git' in dirpath:
            continue
            
        for d in dirnames:
            # 폴더 이름이 "숫자." 으로 시작하는지 확인
            if d.startswith(f"{problem_number}."):
                full_path = os.path.join(dirpath, d)
                print(f" 찾았다! \n📂 위치: {full_path}")
                return full_path
                
    print("\n❌ 폴더를 찾지 못했습니다.")
    return None

def parse_readme_info(readme_path):
    """README.md 내용을 분석해서 커밋 메시지에 쓸 정보를 가져옵니다."""
    info = {"tier": "Unrated", "title": "Unknown", "memory": "0 KB", "time": "0 ms"}
    
    if not os.path.exists(readme_path):
        return None

    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. 헤더 파싱: [Silver IV] 제목 - 번호
    header_match = re.search(r'^# \[(.*?)\] (.*?) - \d+', content, re.MULTILINE)
    if header_match:
        info['tier'] = header_match.group(1)
        info['title'] = header_match.group(2)

    # 2. 성능 파싱: 메모리: 00 KB, 시간: 00 ms
    perf_match = re.search(r'메모리:\s*(.*KB),\s*시간:\s*(.*ms)', content)
    if perf_match:
        info['memory'] = perf_match.group(1)
        info['time'] = perf_match.group(2)
    
    return info

def update_readme_and_commit(base_path, problem_folder_path, target_date_str, mode):
    readme_path = os.path.join(problem_folder_path, "README.md")
    
    # 정보 파싱
    info = parse_readme_info(readme_path)
    if not info:
        print(f"❌ 오류: {problem_folder_path} 안에 README.md가 없습니다.")
        return

    # --- 날짜 및 시간 랜덤 설정 ---
    try:
        dt = datetime.strptime(target_date_str, "%Y-%m-%d")
        
        # 08시 ~ 23시 사이 랜덤 (현실성 부여)
        rand_hour = random.randint(8, 23) 
        rand_min = random.randint(0, 59)
        rand_sec = random.randint(0, 59)
        
        dt = dt.replace(hour=rand_hour, minute=rand_min, second=rand_sec)
        
        # 한국어 포맷 (README용)
        readme_date_text = f"{dt.year}년 {dt.month}월 {dt.day}일 {dt.strftime('%H:%M:%S')}"
        # Git 포맷 (커밋용)
        git_date_str = dt.strftime("%Y-%m-%d %H:%M:%S")
        
    except ValueError:
        print("❌ 날짜 형식이 틀렸습니다.")
        return

    # --- README 내용 수정 ---
    with open(readme_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    is_date_section = False
    
    for line in lines:
        if "### 제출 일자" in line:
            is_date_section = True
            new_lines.append(line)
        elif is_date_section and line.strip() != "":
            new_lines.append(f"{readme_date_text}\n")
            is_date_section = False
        else:
            new_lines.append(line)

    with open(readme_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

    # --- Git 커밋 수행 ---
    relative_folder_path = os.path.relpath(problem_folder_path, base_path)
    commit_msg = f"[{info['tier']}] Title: {info['title']}, Time: {info['time']}, Memory: {info['memory']} -BaekjoonHub"
    
    # 환경변수 설정 (Committer Date 조작을 위해)
    env = os.environ.copy()
    env['GIT_COMMITTER_DATE'] = git_date_str
    
    try:
        # 1. 해당 폴더 add
        subprocess.run(["git", "add", relative_folder_path], cwd=base_path, check=True)
        
        # 2. 커밋 (환경변수 env 전달하여 Committer Date도 조작)
        if mode == '2': # 덮어쓰기 (Amend)
            print("⚡ 기존 커밋을 덮어씁니다 (--amend)...")
            subprocess.run([
                "git", "commit", "--amend", "-m", commit_msg, "--date", git_date_str
            ], cwd=base_path, check=True, env=env)
        else: # 새 커밋 (New)
            print("🌱 새 커밋을 생성합니다...")
            subprocess.run([
                "git", "commit", "-m", commit_msg, "--date", git_date_str
            ], cwd=base_path, check=True, env=env)
            
        print(f"✅ 커밋 완료: {commit_msg}")
        print(f"📅 날짜/시간 설정: {git_date_str}")
        print("⚠️ 주의: GitHub에 반영하려면 'git push -f origin main'을 하세요.")
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Git 오류 발생: {e}")

# --- 메인 실행 ---
if __name__ == "__main__":
    ROOT_DIR = os.getcwd() 
    print(f"📍 현재 작업 위치: {ROOT_DIR}")
    print("--- 🛠️ 백준 잔디 조작기 (Perfect Backdating) ---")

    while True:
        p_num = input("\n문제 번호 (종료: q): ").strip()
        if p_num.lower() == 'q':
            break
            
        target_path = find_problem_path(ROOT_DIR, p_num)
        
        if target_path:
            print("\n[1] 새 커밋 만들기 (New)")
            print("[2] 방금 올린 커밋 덮어쓰기 (Fix/Amend)")
            mode = input("선택 (기본 1): ").strip()
            
            d_str = input("원하는 날짜 (YYYY-MM-DD): ").strip()
            update_readme_and_commit(ROOT_DIR, target_path, d_str, mode)