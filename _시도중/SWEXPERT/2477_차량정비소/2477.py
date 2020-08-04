# import sys
#
# sys.stdin = open('sample_input.txt', 'r')
#
#
# class Customer:
#     def __init__(self, number):
#         self.number = number
#         self.reception_number = 0
#         self.repair_number = 0
#
#
# class Reception:
#     def __init__(self, number, take_time):
#         self.number = number
#         self.take_time = take_time
#         self.customer = None
#         self.work_time = 0
#
#     def receive(self, human):
#         self.customer = human
#
#
#     def work(self):
#         if self.work_time == self.take_time:
#             # 정비창구 대기 큐로 내보낸다.
#
#             # 자신의 work_time을 초기화한다.
#             self.work_time = 0
#             # 손님을 None으로 변경한다.
#             self.customer = None
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N, M, K, A, B = map(int, input().split())
#
#     # 접수창구
#     empty_reception_count = N
#     receptions = list(map(int, input().split()))
#     # 정비창구
#     empty_repair_count = M
#     repairs = list(map(int, input().split()))
#     # 손님들
#     customers = list(map(int, input().split()))
#
#     receptionQ = []
#     repairQ = []
#     print(customers)
