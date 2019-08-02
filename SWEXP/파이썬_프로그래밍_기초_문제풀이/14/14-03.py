'''
다음의 결과와 같이 임의의 URL 주소를 입력받아 protocol, host, 나머지(path, querystring, ...)로

구분하는 프로그램을 작성하십시오.

입력
http://www.example.com/test?p=1&q=2

출력
protocol: http
host: www.example.com
others: test?p=1&q=2
'''

input_url = input()

divider1 = "://"
divider2 = "/"

divider1_idx = input_url.find(divider1)
divider2_idx = input_url.find(divider2,divider1_idx+len(divider1))

protocol = input_url[:divider1_idx]
host = input_url[divider1_idx + len(divider1) : divider2_idx]
others = input_url[divider2_idx+len(divider2):]

print("protocol: {}".format(protocol))
print("host: {}".format(host))
print("others: {}".format(others))



