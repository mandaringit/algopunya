//: [Previous](@previous)

import Foundation

// 강제 추출 (!)
// 가장 간단하지만, 가장 위험한 방법. => 옵셔널 만든 의미가 무색해지기도 함..
var myName:String? = "mandarin"

// 옵셔널 아닌 값은 옵셔널이 못들어가므로 추출하여 할당.
var mandarin:String = myName!

myName = nil
//mandarin = myName! // 오류

if myName != nil {
    print("My name is \(myName!)")
} else {
    print("myName == nil")
}
// 런타임 오류 가능성을 내포하므로 강제 추출 방식은 지양하도록..

//: [Next](@next)
