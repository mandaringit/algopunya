//: [Previous](@previous)

import Foundation

let IntegerValue:Int = 5

switch IntegerValue {
case 0:
    print("Value == zero")
case 1...10:
    print("Value == 1~10")
    fallthrough
case Int.min..<0, 101..<Int.max: // 범위도 가능
    print("Value< 0 or Value > 100")
default:
    print("10 < Value <= 100")
}

let doubleValue:Double = 3.0

switch doubleValue {
case 0:
    print("Value == zero")
case 1.5...10.5 :
    print("1.5 <= Value <= 10.5")
default:
    print("Value == \(doubleValue)")
}


let stringValue:String = "Liam Neeson"

switch stringValue {
case "mandarin":
    print("He is mandarin")
case "Jay":
    print("He is Jay")
case "Jenny","Joker","Nova":
    print("He or She is \(stringValue)")
default:
    print("\(stringValue) said 'I don't know who you are'")
}

let stringValue2:String = "Liam Neeson"

switch stringValue2 {
case "mandarin":
    print("He is mandarin")
case "Jay":
    print("He is Jay")
case "Jenny": // 빈 상태로 두면 에러가 납니다. => fallthrough 쓰세요
    fallthrough
case"Joker":
    fallthrough
case "Nova":
    print("He or She is \(stringValue2)")
default:
    print("\(stringValue2) said 'I don't know who you are'")
}

// 튜플도 가능합니다.
typealias NameAge = (name:String,age:Int)

let tupleValue:NameAge = ("mandarin",99)

switch tupleValue {
case ("mandarin",99):
    print("정확히 맞췄습니다.")
default:
    print("누굴 찾나요?")
}

// 와일드카드 식별자(_)와 함께 사용하면 좀 더 유용하다.

let tupleValue2:NameAge = ("mandarin",99)

switch tupleValue2 {
case ("mandarin",50):
    print("정확히 맞췄습니다.")
case ("mandarin",_):
    print("이름만 맞았습니다. 나이는 \(tupleValue2.age)입니다.")
case (_,99):
    print("나이만 맞았습니다. 이름은 \(tupleValue.name)입니다.")
default:
    print("누굴 찾나요?")
}

// where 키워드를 사용하여 case 조건 확장이 가능하다.
let 직급:String = "사원"
let 연차:Int = 1
let 인턴인가:Bool = false

switch 직급 {
case "사원" where 인턴인가 == true:
    print("인턴입니다.")
case "사원" where 연차 < 2 && 인턴인가 == false:
    print("신입사원입니다.")
case "사원" where 연차 > 5:
    print("연식 좀 된 사원입니다.")
case "사원":
    print("사원입니다.")
case "대리":
    print("대리입니다.")
default:
    print("사장입니까?")
}

// 열거형과 같은 한정된 범위의 값을 입력값으로 받게 될 때 값에 대응하는 각 case를 구현하면
// default를 구현하지 않아도 된다.

enum School {
    case primary, elementary, middle, high, college, university, graduate
}

let 최종학력: School = School.university

switch 최종학력 {
case .primary:
    print("최종학력은 유치원입니다.")
case .elementary:
    print("최종학력은 초등학교입니다.")
case .middle:
    print("최종학력은 중학교입니다.")
case .high:
    print("최종학력은 고등학교입니다.")
case .college, .university:
    print("최종학력은 대학(교)입니다.")
case .graduate:
    print("최종학력은 대학원입니다.")
}

// 열거형에 케이스가 추가될 가능성이 있다면 어떻게 대비하지..? => unknown속성

enum Menu {
    case chicken
    case pizza
    case hamburger
}

let lunchMenu:Menu = .chicken

switch lunchMenu {
case .chicken:
    print("반반 무많이")
case .pizza:
    print("핫소스 많이 주세요")
@unknown case _: // case: default: 와 같은 표현입니다.
    print("오늘 메뉴가 뭐죠?")
}




//: [Next](@next)
