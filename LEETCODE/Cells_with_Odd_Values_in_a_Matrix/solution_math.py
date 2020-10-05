class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:

        row = [0] * n
        col = [0] * m

        for ri, ci in indices:
            # XOR 연산. 0이면 1로, 1이면 0으로.
            # 홀 & 짝 여부만을 판단하기 위해 토글한다고 생각하면 됨.
            row[ri] = row[ri] ^ 1
            col[ci] = col[ci] ^ 1

        row_count = sum(row) * m  # 홀수라고 판단되는 row의 원소 갯수들
        col_count = sum(col) * n  # 짝수라고 판단되는 col의 원소 갯수들
        # 겹친 경우, 홀 + 홀은 짝이므로 불가능한 경우다.
        overlaped = sum(row) * sum(col)
        # row, col이 겹친 원소 갯수를 위에서 두번 더했으므로 두번 빼줌(*2)
        ans = row_count + col_count - 2 * overlaped

        return ans
