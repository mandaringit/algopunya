class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:

        target_idx = 0
        result = []

        for num in range(1, n+1):
            if target[target_idx] == num:
                result.append("Push")
                target_idx += 1
                if target_idx >= len(target):
                    break
            else:
                result.extend(["Push", "Pop"])

        return result
