'''
아래의 상품 딕셔너리 데이터를 가격에 따라 내림차순으로 정렬하는 프로그램을 작성하십시오.


"TV": 2000000,
"냉장고": 1500000,
"책상": 350000,
"노트북": 1200000,
"가스레인지": 200000,
"세탁기": 1000000,
'''


products = {
    "TV": 2000000,
    "냉장고": 1500000,
    "책상": 350000,
    "노트북": 1200000,
    "가스레인지": 200000,
    "세탁기": 1000000,
}

sorted_list = sorted(products,key= lambda k: products[k])
sorted_list.reverse()

for key in sorted_list:
    print("{}: {}".format(key,products[key]))





