//: [Previous](@previous)

import Foundation

// 정수타입.
// Int : +, - 부호를 포함한 정수
// UInt : 이 중, - 부호를 포함하지 않는 0을 포함한 양의 정수는 UInt

// ! Int 최댓값 <= "요 사잇값" <= UInt 최댓값 ~ 을 이용하는 경우를 제외하면 그냥 Int 쓰자.

var integer: Int = -100
let unsignedInteger:UInt = 50 // 음수 할당 불가
print("Integer 값:\(integer), unsignedInteger 값:\(unsignedInteger)")
print("Int 최댓값:\(Int.max), Int 최솟값:\(Int.min)")
print("UInt 최댓값:\(UInt.max), UInt 최솟값:\(UInt.min)")
let largerInteger:Int64 = Int64.max
let smallUnsignedInteger:UInt8 = UInt8.max
print("Int64 최댓값:\(largerInteger), UInt8 최댓값:\(smallUnsignedInteger)")

//let tooLarge:Int = Int.max + 1 // overflow
//let cannotBeNegative: UInt = -5 // 음수 안대죵

//integer = unsignedInteger // Int와 UInt는 다른 타입.
integer = Int(unsignedInteger)

// 진법에 따른 표현법
let decimalIntger:Int = 28
let binaryInteger:Int = 0b11100
let octalIntger:Int = 0o34
let hexadecimalInteger:Int = 0x1C

//: [Next](@next)
