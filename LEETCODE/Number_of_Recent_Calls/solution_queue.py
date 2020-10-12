from collections import deque


class RecentCounter:

    def __init__(self):
        self.requests = deque()
        self.left = -3000
        self.right = 0

    def ping(self, t: int) -> int:
        self.left = t - 3000
        self.right = t

        while self.requests and self.requests[0] < self.left:
            self.requests.popleft()

        self.requests.append(t)

        return len(self.requests)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
