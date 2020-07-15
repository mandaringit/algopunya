//: [Previous](@previous)

import Foundation

// 이미 존재하는 데이터타입에 임의로 다른 이름을 부여할 수 있다.
// 그 다음 기본 타입 이름과 이후에 추가한 별칭을 모두 사용 가능하다.

typealias MyInt = Int
typealias YourInt = Int
typealias MyDouble = Double

let age:MyInt = 100
var yaer: YourInt = 100

// MyInt도, YourInt도 Int이기 때문에 같은 타입으로 취급
yaer = age
let month:Int = 7
let pecentage:MyDouble = 99.9

//: [Next](@next)
