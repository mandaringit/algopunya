class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def generate(l, r, form):
            if l == 0 and r == 0:  # 결과 넣기
                result.append("".join(form))
            elif l == r:  # 0은 아니고 왼쪽이랑 오른쪽 같을때
                generate(l-1, r, form+["("])
            elif l < r:
                if l > 0:
                    generate(l-1, r, form+["("])
                generate(l, r-1, form+[")"])

        generate(n, n, [])
        return result
