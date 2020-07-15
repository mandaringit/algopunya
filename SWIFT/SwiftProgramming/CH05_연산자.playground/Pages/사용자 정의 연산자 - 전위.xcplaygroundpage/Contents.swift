//: [Previous](@previous)

import Foundation

// ###### 사용자 정의 전위 연산자 ######

prefix operator **

prefix func ** (value:Int) -> Int {
    return value * value
}

let minusFive:Int = -5
let sqrtMinusFive = **minusFive


// 기존에 있던 연산자 재정의 -> 함수 재정의

prefix func ! (value:String) -> Bool {
    return value.isEmpty
}

var stringValue:String = "mandarin"
var isEmptyString:Bool = !stringValue

stringValue = ""
isEmptyString = !stringValue

// 앞에서 만든 ** 연산자 중복정의

prefix operator **
prefix func ** (value:String) -> String {
    return value + " " + value
}

let resultString:String = **"mandarin"




//: [Next](@next)
