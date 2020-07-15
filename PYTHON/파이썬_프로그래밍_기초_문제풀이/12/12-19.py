'''
리스트 내포 기능을 이용해 [12, 24, 35, 70, 88, 120, 155]에서

홀수번째 항목을 제거한 후 리스트를 출력하는 프로그램을 작성하십시오.
'''

sample_list = [12, 24, 35, 70, 88, 120, 155]

print([number for idx,number in enumerate(sample_list) if (idx+1) %2 ==0])