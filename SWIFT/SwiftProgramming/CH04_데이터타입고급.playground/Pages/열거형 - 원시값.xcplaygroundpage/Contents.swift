//: [Previous](@previous)
import Foundation

// 열거형 각 항목은 자체로도 하나의 값이지만, 항목의 원시 값(raw Value)도 가질 수 있다.

// 타입 명시,
enum School:String {
    case primary = "유치원"
    case elementary = "초등학교"
    case middle = "중학교"
    case high = "고등학교"
    case college = "대학"
    case university = "대학교"
    case graduate = "대학원"
}

let higestEducationLevel:School = School.university
// .rawValue로 쓰자
print("저의 최종 학력은 \(higestEducationLevel.rawValue) 졸업입니다.")

enum WeekDays:Character {
    case mon="월",tue="화",wed="수",thu="목",fri="금",sat="토",sun="일"
}

let today:WeekDays = .fri
print("오늘은 \(today.rawValue)요일 입니다.")

// 일부만 원시값을 주면 해도 좋다.
// 문자열은 각 항목 이름을 그대로 원시값으로 갖으며,
// 정수타입은 첫 항목을 기준으로 0부터 1씩 늘어난 값을 갖는다.

enum School2:String{
    case primary = "유치원"
    case elementary = "초등학교"
    case middle = "중학교"
    case high = "고등학교"
    case college
    case university
    case graduate
}

let higestEducationLevel2:School2 = .university
print("저의 최종 학력은 \(higestEducationLevel2.rawValue) 졸업입니다.")

print(School2.elementary.rawValue)

enum Numbers:Int{
    case zero,one,two,ten = 10
}

print("\(Numbers.zero.rawValue), \(Numbers.one.rawValue), \(Numbers.two.rawValue), \(Numbers.ten.rawValue)")

// 원시값을 갖는 열거형일 때, 열거형의 원시 값 정보를 안다 ? => 원시 값을 통해 열거형 변수 또는 상수 생성 가능
let primary = School(rawValue:"유치원")
let graduate = School(rawValue:"석박사") // nil

let one = Numbers(rawValue:1)
let three = Numbers(rawValue:3)

//: [Next](@next)
