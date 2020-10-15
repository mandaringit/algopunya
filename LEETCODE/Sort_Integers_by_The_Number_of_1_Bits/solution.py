class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda x: [bin(x).count('1'), x])

    """
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort()

        bit_counter = {}
        for num in arr:
            n = num
            count = 0
            while n != 0:
                n, r = divmod(n, 2)
                count += r

            if count in bit_counter:
                bit_counter[count].append(num)
            else:
                bit_counter[count] = [num]

        result = []
        for key in sorted(bit_counter):
            result.extend(bit_counter[key])

        return result
    """
