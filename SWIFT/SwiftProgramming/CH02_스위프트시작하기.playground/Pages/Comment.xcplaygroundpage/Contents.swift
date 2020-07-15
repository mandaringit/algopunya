//: [Previous](@previous)

import Foundation

// 한줄 주석
// 한줄 주석은 이렇게 표현

// 1. 여러줄 주석
/*
 여러줄 주석을 시작할 때는 슬래시별표
*/

// 2. 중첩 주석
/*
주석안에
 /*
 주석안에
    // 한줄 주석
 */
*/

// 3. 마크업 문법을 활용한 문서화 주석

/// 오류 타입의 열거형입니다.
/// - noName: 이름을 전달받지 못헸을 때 발생하는 오류
/// - incorectAge(age:Int): 나이가 0세 미만, 150세 초과인 경우 잘못된 나이로 인식하여
/// 오류로 처리
/// - unknown : 알 수 없는 오류
enum HelloError : Error {
    case noName
    case incorrectAge(age:Int)
    case unknown
}

/**
 여기에 작성되는 텍스트는 Description 부분에 표기된다.
 
 텍스트 간에 한 줄을 비워놓으면 줄바꿀이 된다.
 
 '-','+','*'를 사용하여 원형 글머리 기호를 사용 가능
 - 이렇게
 + 이렇게
 * 이렇게
 
 아니면 번호로 글머리 기호 매기기 가능
 
 1. 1번
 2. 2번
 6. 3번
 
 눈치챘겠지만 앞에 붙는 번호는 크게 중요하지 않다.
 
 ---
 
 문단 바꿈
 
 ---
 
 언더바 또는 별표를 사용해 텍스트 강조 가능
 
 텍스트를 기울이려면 *A pair of marks* 를 사용
 
 텍스트를 굵게 표기하려면 **Two Pair of marks**
 
 관련 링크도 가능
 
 [Swift Blog](http://swift.org/blog/)
 
 ---
 
 등호를 사용하면 바로 위 텍스트를 큰 제목으로 표시한다. #도 동일하다.
 
 큰 제목 표시
 ===
 
 바를 사용하면 바로 위 텍스트를 중간 크기 제목으로 표시
 
 중간 제목 표시
 ---
 
 다른 텍스트보다 네 칸 이상 들여쓰기 하면 코드블록 생성. ` 세개도 가능.
        // 코멘트 가능
 
            let myName :String
            try helloSwift(myName,yourAge:100)
 ```
 let myName :String
 try helloSwift(myName,yourAge:100)
 ```
 
 Precondition, PostCondition, Requires, ..  등의 키워드를 통해 적절한 정보를 제공해라
 
 - note: 강조하고싶은 메모를 노트로 남긴다
 - author: 작성자를 남긴다
 - warning: 주의해야할 점을 남길 수 있다. *주의 : 하등 쓸모없는 함수임
 
 ---
 > 매개 변수와 반환 값 등도 적절히 표기 가능
 - parameters:
    - yourName: 당신의 이름.
    - yourAge: 당신의 나이. 0 미만 또는 150을 초과하면 오류 발생
- Throws: 오류가 발생하면 HelloError의 한 케이스를 throw
- returns: Hello String
 **/
func helloSwift(yourName:String?,yourAge age:Int = 0) throws -> String {
    guard let name:String = yourName else {
        throw HelloError.noName
    }
    
    if age > 150 {
        throw HelloError.incorrectAge(age: age)
    }
    
    return "Hello Swift!! My Name is \(name)." + (age > 0 ? "I'm \(age) yaers old." : "")
}


//: [Next](@next)
