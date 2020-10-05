class Solution:
    def removeOuterParentheses(self, S: str) -> str:

        pair = 0
        result = []
        for parentheses in S:
            if parentheses == '(':
                if pair != 0:
                    result.append(parentheses)
                pair += 1
            else:
                pair -= 1
                if pair != 0:
                    result.append(parentheses)

        return "".join(result)

    # def removeOuterParentheses(self, S: str) -> str:

    #     pair = 0
    #     result = []
    #     for parentheses in S:

    #         if pair == 0:
    #             if parentheses == '(':
    #                 pair += 1
    #         else:
    #             if parentheses == '(':
    #                 result.append(parentheses)
    #                 pair += 1
    #             else:
    #                 pair -= 1
    #                 if pair != 0:
    #                     result.append(parentheses)

    #     return "".join(result)
