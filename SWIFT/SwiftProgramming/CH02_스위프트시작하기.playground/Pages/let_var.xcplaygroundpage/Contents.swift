//: [Previous](@previous)

import Foundation

// 변수는 생성 후 데이터 값을 변경할 수 있다.
// 상수는 한번 값을 설정하면 다음에 변경할 수 없다.

// 타입 추론은 스위프트에 많이 익숙해지고 나서 쓰라.

// 1. 변수
// var [변수명]: [데이터타입] = [값]

var name:String = "mandarin"
var age:Int = 100
var job = "IOS DEVELOPER" // 타입추론
var height = 181.5 // 더블, 타입추론
print("\(type(of:height))")

age = 99 // 변수라서 변경 가능
job = "Writer" // 변경시, 기존과 같은 타입의 값을 할당해야한다.
print("저의 이름은 \(name) 이고, 나이는 \(age)세이며, 직업은 \(job)입니다. 비밀이지만, 키는 \(height)센티미터 입니다.")

// 2. 상수
// let [변수명]: [데이터타입] = [값]
// 상수 생성 때도 데이터 타입 생략은 가능하다.

let name2:String = "mandarin"
var age2:Int = 100
var job2="IOS DEVELOPER"
let height2=181.5
job2 = "Writer"
name2 = "엥엥" // 오류 발생

/*
 상수를 사용하는 이유는 가독성. 상수는 변하지 않는다. 차후 값을 신경쓰지 않아도 된다는 점.
 
 또, 특정 값에 특별한 의미를 부여할 때 상수를 사용.
 */


//: [Next](@next)
