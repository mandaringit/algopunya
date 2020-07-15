//: [Previous](@previous)

import Foundation

// ###### 사용자 정의 후위 연산자 ######

postfix operator **

postfix func ** (value:Int) -> Int {
    return value + 10
}

let five: Int = 5
let fivePlusTen:Int = five**

// 하나의 피연산자에 전위연산 , 후위연산을 한줄에 쓰면 후위 연산 먼저 수행
prefix operator **
prefix func ** (value:Int) -> Int {
    return value * value
}

let sqrtFivePlusTen:Int = **five**

//: [Next](@next)
