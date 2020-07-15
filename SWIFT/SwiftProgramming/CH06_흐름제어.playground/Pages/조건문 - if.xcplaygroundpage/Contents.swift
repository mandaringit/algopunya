//: [Previous](@previous)

import Foundation

// 정수, 실수 등 0이 아닌 모든 값을 참으로 취급하여 조건 값이 될 수 있었던 다른 언어와는달리,
// 스위프트의 if 구문은 조건의 값이 "반드시 Bool타입" 이어야한다.

let first:Int = 5
let second:Int = 7

if first > second {
    print("first > second")
} else if (first < second) { // 소괄호는 선택사항.
    print("first < second")
} else {
    print("first == second")
}



//: [Next](@next)
