//: [Previous](@previous)

import Foundation

/* 반복적인 데이터나 시퀀스를 다룰 때 많이 사용한다.
 
 for 임시 상수 in 시퀀스 아이템 {
    실행 코드
 }
 
 */

for i in 0...2 {
    print(i)
}

for i in 0...5{
    
    if i.isMultiple(of:2){
        print(i)
        continue
    }
    
    print("\(i) == 홀수")
}

let helloSwift:String = "Hello Swift!"

for char in helloSwift{
    print(char)
}

var result:Int = 1

for _ in 1...3 {
    result *= 10
}

print("10의 3제곱은 \(result)입니다.")

// 기본 컬렉션 타입에도 유용하게 사용가능하다.

// 딕셔너리
let friends:[String:Int] = ["Jay":35,"Joe":29,"Jenny":31]

for tuple in friends{
    print(tuple)
}

let 주소: [String:String] = ["도":"충청북도","시군구":"청주시 청원구","동읍면":"율량동"]

for (키,값) in 주소 {
    print("\(키) : \(값)")
}

let 지역번호: Set<String> = ["02","031","032","033","041","042","051","061"]

for 번호 in 지역번호{
    print(번호)
}

// 옵셔널, 클로저 등을 배우고 함수형 패러다임에 익숙해지면 map,filter,flatMap등을 더 많이 사용하게 된다..

//: [Next](@next)
