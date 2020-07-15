//: [Previous](@previous)

import Foundation

// 종료되지 않는 함수 => 정상적으로 끝나지 않는 함수 (비반환 함수, 비반환 메서드)
// 정상적으로 끝날 수 없는 함수
// 비반환 메서드는 재정의 가능하지만 비반환 타입이라는 것은 변경 불가하다.

func crashAndBurn() -> Never {
    fatalError("Somthing Very, very bad happend")
}

//crashAndBurn()

func someFunction(isAllIsWell:Bool){
    guard isAllIsWell else {
        print("마을에 도둑이 들었습니다!")
        crashAndBurn()
    }
    print("All is well")
}

someFunction(isAllIsWell:true)
someFunction(isAllIsWell:false)

//: [Next](@next)
