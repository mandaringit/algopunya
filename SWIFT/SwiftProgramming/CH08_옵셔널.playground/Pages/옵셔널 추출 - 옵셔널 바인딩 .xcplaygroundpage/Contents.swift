//: [Previous](@previous)

import Foundation

var myName: String? = "mandarin"

// 옵셔널 바인딩을 통한 임시 상수 할당
if let name = myName {
    print("My name is \(name)")
} else {
    print("myName == nil")
}

if var name = myName {
    name="wizplan" // 변수이므로 내부 변경 가능
    print("My name is \(name)")
} else {
    print("myName == nil")
}

var myName2: String? = "mandarin"
var yourName:String? = nil

// friend가 nil이므로 실행 안됨
if let name = myName2, let friend = yourName {
    print("We are friend! \(name) & \(friend)")
}

yourName = "eric"

if let name = myName2, let friend = yourName{
    print("We are friend! \(name) & \(friend)")
}


//: [Next](@next)
