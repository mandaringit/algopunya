# 리스트
myList = [1, 2, 3, 4]
newList = myList[:]
newList2 = list(myList)

# Set
people = {"버피", "에인절", "자일스"}
slayers = people.copy()  # 셋의 깊은 복사
slayers.discard("자일스")
people.remove("에인절")
print(slayers)
print(people)

# Dict
myDict = {"안녕": "세상"}
newDict = myDict.copy()

# 기타 객체
import copy

myObj = "다른 어떤 객체"
newObj = copy.copy(myObj)  # 얕은 복사
newObj2 = copy.deepcopy(myObj)
