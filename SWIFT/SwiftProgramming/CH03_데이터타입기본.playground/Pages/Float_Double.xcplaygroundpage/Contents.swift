//: [Previous](@previous)

import Foundation

// 흔히 말하는 소수점 자리가 있는 수.

// 부동소수 타입은 정수 타입보다 훨씬 넓은 범위의 수를 표현 가능함

// Double : 64비트 부동소수
// Float : 32비트 부동소수

// 무엇을 쓸지 잘 모르겠네.. => Double!

// Float이 수용할 수 있는 범위를 넘어선다 => 정확도가 떨어진다.
var floatValue:Float = 1234567890.1

// Double은 충분히 수용 가능하다.
var doubleValue:Double = 1234567890.1

print("floatValue: \(floatValue) doubleValue: \(doubleValue)")

// Float이 수용할 수 있는 범위의 수로 변경한다
floatValue = 123456.1

// 문자열 보간법을 사용하지 않고 단순히 변수 또는 상수의 값만 보고 싶으면
// print 함수의 전달인자로 변수 또는 상수를 전달하면 된다.
print(floatValue)

// 스위프트 4.2부터 랜덤수를 만드는 메서드가 생겼다.
Int.random(in:-100...100)
UInt.random(in:1...30)
Double.random(in:1.5...4.3)
Float.random(in: -0.5...1.5)

//: [Next](@next)
