#-*- coding:utf-8 -*-

'''
다음과 같이 사용자 2명으로부터 가위, 바위, 보를 입력 받아

가위, 바위, 보 규칙이 정의된 함수를 이용해 승패를 결정하는 코드를 작성하십시오.
'''

def user_input():
    user1 = input()
    user2 = input()

def game_answer_input():
    user1_ans = input()
    user2_ans = input()
    return user1_ans,user2_ans

def game(ans):
    user1_ans = ans[0]
    user2_ans = ans[1]
    if user1_ans == user2_ans :
        print("비겼습니다.")
    elif user1_ans == "가위" :
        if user2_ans == "바위":
            print("바위가 이겼습니다!")
        else :
            print("가위가 이겼습니다!")
    elif user1_ans == "바위" :
        if user2_ans == "가위":
            print("바위가 이겼습니다!")
        else :
            print("보가 이겼습니다!")
    else :
        if user2_ans == "가위":
            print("가위가 이겼습니다!")
        else :
            print("보가 이겼습니다!")

user_input()
game(game_answer_input())