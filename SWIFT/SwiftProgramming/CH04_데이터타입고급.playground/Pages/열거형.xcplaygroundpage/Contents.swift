//: [Previous](@previous)

import Foundation

// 연관된 항목들을 묶어서 표현할 수 있는 타입
// 배열, 딕셔너리같은 타입과 다르게 프로그래머가 정의해준 항목 값 외에는 추가/수정 불가함
// 딱 정해진 값만 열거형 값에 속할 수 있다.

/*
요긴하게 쓰이는 경우
- 제한된 선택지를 주고싶을 때
- 정해진 값 외에는 입력받고 싶지 않을때
- 예상된 입력 값이 한정되어 있을 때
*/

// 스위프트 열거형은 각 항목이 그 자체로 고유의 값이 될 수 있다.

// 열거형 각 항목이 원시 값 이라는 형태로 실제 값을 가질 수 있다.
// 연관 값을 사용해 다른 언어에서 공요체라고 불리는 값의 묶음도 구현 가능하다.
// switch 구문과 만날때 멋지게 활용 가능.

// 옵셔널은 열거형으로 구현되어 있다.

// 기본 열거형 - enum
// 각 항목은 자체가 고유값.
enum School {
    case primary
    case elementary
    case middle
    case high
    case collage
    case university
    case graduate
}

// 한줄 선언도 가능
enum School2{
    case primary,elementary,middle,high,collage,university,graduate
}

// 둘 다 동일한 표현
var highestEducationalLevel:School = School.university
var highestEducationalLevel2:School = .university

// 같은 타입인 School 내부의 항목으로만 highestEducationalLevel의 값을 변경 가능
highestEducationalLevel = .graduate
type(of:highestEducationalLevel)

//: [Next](@next)
