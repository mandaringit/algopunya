import time


def test_1_input(testing_fn):

    answer_list = []

    with open('output.txt', 'r') as out:
        answers = out.readlines()

        for answer in answers:
            clean_answer = answer.replace("\n", "").strip()
            answer_list.append(clean_answer)

    with open('input.txt', 'r') as f:
        lines = f.readlines()

        test_case_number = int(lines[0].replace("\n", ""))

        start_time = time.time()
        for idx, test_input in enumerate(lines[1:]):
            # 여기에 측정 할 함수를 넣자 #

            clean_test_input = test_input.replace("\n", "")
            result = f"#{idx+1} {testing_fn(clean_test_input)}"
            if result.strip() == answer_list[idx]:
                print(f"{result} ✅")
            else:
                print(f"{result} ❌=> {answer_list[idx]}")

            #----------------------------#
        end_time = time.time()
        print(f"실행시간 => {round((end_time - start_time)*1000)} ms")


# def test_2_input(testing_fn):

#     answer_list = []

#     with open('output.txt', 'r') as out:
#         answers = out.readlines()

#         for answer in answers:
#             clean_answer = answer.replace("\n", "").strip()
#             answer_list.append(clean_answer)

#     with open('input.txt', 'r') as f:
#         lines = f.readlines()

#         test_case_number = int(lines[0].replace("\n", ""))

#         start_time = time.time()
#         for idx, test_input in enumerate(lines[1:]):
#             # 여기에 측정 할 함수를 넣자 #

#             clean_test_input = test_input.replace("\n", "")
#             result = f"#{idx+1} {testing_fn(clean_test_input)}"
#             if result.strip() == answer_list[idx]:
#                 print(f"{result} ✅")
#             else:
#                 print(f"{result} ❌=> {answer_list[idx]}")

#             #----------------------------#
#         end_time = time.time()
#         print(f"실행시간 => {round((end_time - start_time)*1000)} ms")
