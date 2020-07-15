def solution(arr):
    answer = []

    for i in range(len(arr)):
        if i == 0:
            answer.append(arr[i])
        else:
            if arr[i] != arr[i-1]:
                answer.append(arr[i])

    return answer

# 여러 방법이 있을 수 있겠따


"""
def solution(arr):
    answer = []
    
    for idx,num in enumerate(arr):
        if idx == 0:
            answer.append(num)
        else:
            if num != arr[idx-1]:
                answer.append(num)
    
    return answer
"""
