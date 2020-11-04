import os

question_name = input("문제 이름을 입력해주세요.")

underbar_name = question_name.strip().replace(" ", "_")
directory = f"LEETCODE/{underbar_name}"

if not os.path.isdir(directory):
    print(f"{directory} 폴더를 생성합니다.")
    os.mkdir(directory)

    with open(f"LEETCODE/{underbar_name}/solution.py", 'w') as f:
        print(f"solution.py 생성 완료")

    with open(f"LEETCODE/{underbar_name}/solution.ts", 'w') as f:
        print(f"solution.ts 생성 완료")

    with open(f"LEETCODE/{underbar_name}/README.md", 'w') as f:
        f.write(f"# [LEETCODE] {question_name}\n\n")
        f.write(f"### 접근")
        print("README.md 생성 완료")
else:
    print("경로가 이미 존재합니다.")
