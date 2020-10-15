class Solution:
    def average(self, salary: List[int]) -> float:
        min_sal, max_sal = salary[0], salary[0]
        total = 0
        for sal in salary:
            total += sal
            min_sal = min(min_sal, sal)
            max_sal = max(max_sal, sal)

        return (total - min_sal - max_sal) / (len(salary) - 2)
