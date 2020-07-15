//: [Previous](@previous)

import Foundation

// 배열
// let => 변경 불가한 배열 / var => 변경 가능한 배열

// 대괄호를 사용해 배열임을 표현한다.
var names: Array<String> = ["mandarin","twodarin","Threedarin","fourdarin"]

var names2: [String] = ["mandarin","twodarin","Threedarin","fourdarin"]

var emptyArray:[Any] = [Any]()
var emptyArray2:[Any] = Array<Any>()

// 배열 타입을 정확히 명시해줬다면 [] 만으로도 빈배열을 생성할 수있다.
var emptyArray3:[Any] = []
print(emptyArray.isEmpty)
print(names.count)

// 배열은 각 요소에 인덱스를 통해 접근할 수 있다. 인덱스는 0부터 시작한다.
// 잘못된 인덱스에 접근하려고 하면 익셉션 오류가 발생한다.
// 맨처음 , 맨 마지막은 first, last 프로퍼티로 접근 가능하다.

print(names[2])
names[2] = "jenny"
print(names[2])
//print(names[4]) // 인덱스 레인지 아웃
//names[4] = "elsa" // 인덱스 레인지 아웃
names.append("elsa")
names.append(contentsOf:["John","max"])
names.insert("happy", at: 2) // 해당 인덱스에 삽입
names.insert(contentsOf:["Jinhee","minsoo"], at: 5)

print(names[4])
//print(names.firstIndex(of: "mandarin"))
//print(names.firstIndex(of: "christal"))
//print(names.first)
//print(names.last)

let firstItem:String = names.removeFirst()
let lastItem:String = names.removeLast()
let indexZeroItem:String = names.remove(at:0)

print(firstItem)
print(lastItem)
print(indexZeroItem)
print(names[1...3])
//: [Next](@next)
