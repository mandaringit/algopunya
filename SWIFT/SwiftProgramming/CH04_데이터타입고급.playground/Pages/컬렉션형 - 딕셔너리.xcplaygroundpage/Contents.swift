//: [Previous](@previous)

import Foundation

// 순서 없이 키, 쌍으로 구성되는 컬렉션 타입
// let => 변경 불가 딕셔너리 / var => 변경 가능 딕셔너리

// typealias를 통해 조금 더 단순하게 표현 가능
typealias StringIntDictionary = [String:Int]

// 키는 String, 값은 Int인 빈 딕셔너리 생성
var numberForName:Dictionary<String,Int> = Dictionary<String,Int>()
var numberForName2:[String:Int] = [String:Int]()
var numberForName3:StringIntDictionary = StringIntDictionary()

// 키, 값 타입을 명시했다면 [:]로도 가능.
var numberForName4:[String:Int] = [:]

// 초깃값 주어 생성 가능
var numberForName5:[String:Int] = ["mandarin":100,"chulsoo":200,"jenny":300]

print(numberForName.isEmpty)
print(numberForName5.count)

// 키로 접근 가능. 키는 유일. 없는 키로 접근해도 오류 발생 안함. => nil 반환.
// 제거는 removeValue(forkey:)

print(numberForName5["chulsoo"])
print(numberForName5["minji"])

numberForName5["chulsoo"] = 150
print(numberForName5["chulsoo"])

numberForName5["max"] = 999
print(numberForName5["max"])

print(numberForName5.removeValue(forKey: "mandarin"))

print(numberForName5.removeValue(forKey: "mandarin"))

// 키에 해당하는 값이 없으면 기본값 반환.
print(numberForName5["mandarin",default:0])

//: [Next](@next)
