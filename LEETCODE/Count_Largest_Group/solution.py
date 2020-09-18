class Solution:
    def countLargestGroup(self, n: int) -> int:
        # grouping 최대 O(N * 4)
        groups = {}
        for i in range(1, n + 1):
            base = i
            total = 0
            while base // 10 != 0:
                q, r = divmod(base, 10)
                total += r
                base = q

            total += base

            if total in groups:
                groups[total].append(i)
            else:
                groups[total] = [i]

        # 그룹 길이별로 갯수 카운팅. O(N)
        count = 0
        max_len = 0
        for group in groups.values():
            length = len(group)
            if length > max_len:
                max_len = length
                count = 1
            elif length == max_len:
                count += 1

        return count


sol = Solution()

sol.countLargestGroup(174)
