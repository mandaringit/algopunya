//: [Previous](@previous)

import Foundation

// 열거형 항목의 연관 값이 열거형 자신의 값이고자 할 때 사용한다.
// indirect 키워드를 쓴다.
// 특정 항목 : case 키워드 앞 / 열거형 전체: enum 키워드 앞 에 선언해주자

enum ArithmeticExpression {
    case number(Int)
    indirect case addition(ArithmeticExpression, ArithmeticExpression)
    indirect case multiplication(ArithmeticExpression,ArithmeticExpression)
}

indirect enum ArithmeticExpression2 {
    case number(Int)
    case addition(ArithmeticExpression2,ArithmeticExpression2)
    case multiplication(ArithmeticExpression2,ArithmeticExpression2)
}

let five = ArithmeticExpression2.number(5)
let four = ArithmeticExpression2.number(4)
let sum = ArithmeticExpression2.addition(five,four)
let final = ArithmeticExpression2.multiplication(sum,ArithmeticExpression2.number(2))

// 순환 함수
func evaluate(_ expression:ArithmeticExpression2) -> Int {
    switch expression {
    case .number(let value):
        return value
    case .addition(let left, let right):
        return evaluate(left) + evaluate(right)
    case .multiplication(let left, let right):
        return evaluate(left) * evaluate(right)
    }
}

let result: Int = evaluate(final)
print("(5+4)*2 = \(result)")

// 이진 탐색 트리 등의 순환 알고리즘을 구현할때 유용하게 사용한다.

//: [Next](@next)
