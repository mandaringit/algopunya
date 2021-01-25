from typing import List


class Solution:
    # with lambda
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs, digit_logs = [], []

        for log in logs:
            if log.split()[1].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append(log)

        # The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.
        letter_logs.sort(key=lambda x: (x.split()[1:], x.split()[0]))

        # The digit-logs should be put in their original order.
        return letter_logs + digit_logs
