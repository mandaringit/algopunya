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

    interview_file = input(
        '인터뷰 문제풀이 파일을 생성할까요? (Y/N) ---> solution.interview.py')

    if interview_file.lower() == 'y':
        with open(f"LEETCODE/{underbar_name}/solution.interview.py", 'w') as f:
            print(f"solution.interview.py 생성 완료")
    else:
        print("인터뷰 파일은 생략합니다.")
else:
    print("경로가 이미 존재합니다.")
