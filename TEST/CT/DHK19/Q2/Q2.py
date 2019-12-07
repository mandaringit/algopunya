def solution(message, K):
    # write your code in Python 3.6
    msg_splited = message.split(' ')
    print(msg_splited)

    result = ''
    for idx, msg in enumerate(msg_splited):
        if idx == 0 and len(msg) <= K:
            result += msg
        else:
            word_length = len(msg)
            if len(result) + (word_length + 1) <= K:
                result += f" {msg}"
            else:
                break

    return result



print(solution('Codility', 9))
