case_number = int(input())

for loop_number in range(case_number):

    case = input()
    madi = ""

    for idx, char in enumerate(case):

        if idx != len(case)-1:
            if len(madi) == 0:
                madi += char
            elif madi[0] != case[idx]:
                madi += char
            else:
                compare_word = case[idx:idx+len(madi)]
                if madi == compare_word:
                    break
                else:
                    madi += char

    print(f"#{loop_number+1} {len(madi)}")


# 테스트
"""
case = "GALAXYGALAXYGALAXYGALAXYGALAX"

madi = ""

for idx, char in enumerate(case):
    
    if idx != len(case)-1:
        if len(madi) == 0:
            madi+= char
        elif madi[0] != case[idx]:
            madi+= char
        else:
            # madi와 길이가 같은 그 다음 단어를 구한다
            compare_word = case[idx:idx+len(madi)]
            print(madi,compare_word)
            if madi == compare_word:
                break
            else:
                madi+= char
    else:
        print("end")
print(madi)
"""
