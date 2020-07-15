//: [Previous](@previous)

import Foundation

// 안정성을 문법으로 담보하는 문법.
// 옵셔널을 읽을 땐, "해당 변수 또는 상수에는 값이 없을 수 있다.
// 즉, 변수 또는 상수가 nil일 수도 있으므로 사용에 주의하라." 라는 뜻으로 받아들인다.

// 오류가 발생하는 nil 할당
var myName:String = "mandarin"
//myName = nil // 오류!

// nil은 옵셔널로 선언된 곳에서만 사용 가능하다.
var myName2:String? = "mandarin"
print(myName2)
myName2 = nil
print(myName2)

// 옵셔널은 열거형으로 정의되어있다..
func checkOptionValue(value optionValue:Any?){
    switch optionValue {
    case .none:
        print("This Optional variable is nil")
    case .some(let value):
        print("Value is \(value)")
    }
}

var myName3:String? = "mandarin"
checkOptionValue(value:myName3)

myName3 = nil
checkOptionValue(value:myName3)

let numbers:[Int?] = [2,nil,-4,nil,100]

for number in numbers {
    switch number {
    case .some(let value) where value<0:
        print("Negative value!! \(value)")
    case .some(let value) where value > 10:
        print("Large value!! \(value)")
    case .some(let value):
        print("Value \(value)")
    case .none:
        print("nil")
    }
}

//: [Next](@next)
