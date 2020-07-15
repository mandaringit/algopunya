//: [Previous](@previous)

import Foundation

// 연산자가 어디에 위치하느냐도 중요하지만, 공백도 중요하니 잘 살필것

// 나머지연산, 나누기 연산자
let number:Double = 5.0
var result:Double = number.truncatingRemainder(dividingBy:1.5)
result = 12.truncatingRemainder(dividingBy:2.5)

var result2:Int = 5/3
result = 10/3

// 삼항연산자
var valueA:Int = 3
var valueB:Int = 5
var biggerValue:Int = valueA > valueB ? valueA : valueB

valueA = 0
valueB = -3
biggerValue = valueA > valueB ? valueA : valueB

var stringA:String = ""
var stringB:String = "String"
var resultValue:Double = stringA.isEmpty ? 1.0 : 0.0
resultValue = stringB.isEmpty ? 1.0 : 0.0


// 오버플로 연산자 -> 오버플로에 대한 이해 필요
var unsingedInteger:UInt8 = 0
//let errorUnderflowResult:UInt8 = unsingedInteger -1
let underflowedValue:UInt8 = unsingedInteger &- 1

unsingedInteger = UInt8.max
//let errorOverflowResult2:UInt8 = unsingedInteger + 1
let overflowedValue:UInt8 = unsingedInteger &+ 1

// nil 병합 연산자 A ?? B => 옵셔널에서 유용함
// 옵셔널 강제 추출 연산자 O!
// 옵셔널 연산자 V?



//: [Next](@next)
