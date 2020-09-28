class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.q = [-1] * k
        self.front = -1
        self.rear = -1
        self.k = k
        self.size = 0

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        # 가득 ?
        if self.isFull():
            return False

        if self.front == -1:
            self.front = 0
        # 비었나 ?
        self.rear = (self.rear + 1) % self.k
        self.q[self.rear] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        # empty
        if self.isEmpty():
            return False

        self.q[self.front] = -1
        self.front = (self.front + 1) % self.k
        self.size -= 1

        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty():
            return -1

        return self.q[self.front]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return -1

        return self.q[self.rear]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """

        return self.size == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.size == self.k


# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(3)
# print(obj.enQueue(6))
# print(obj.Rear())
# print(obj.Rear())
print(obj.enQueue(1))
print(obj.enQueue(2))
print(obj.enQueue(3))
print(obj.enQueue(4))
print(obj.Rear())
print(obj.isFull())
print(obj.deQueue())
print(obj.enQueue(4))
print(obj.Rear())
