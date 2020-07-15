//: [Previous](@previous)

import Foundation

// 때때로 열거형에 포함된 모든 케이스를 알아야 할 때가 있다.
// 열거형의 이름 뒤에 : 작성하고 CaseInterable 프로토콜 을 채택. => 열거형에 allCases라는 이름의 타입 프로퍼티를 통해 모든 케이스의 컬렉션 생성

enum School: CaseIterable{
    case primary
    case elementary
    case middle
    case high
    case college
    case university
    case graduate
}

let allCases:[School] = School.allCases
print(allCases)

// 원시값을 같는 열거형이라면, 원시값 타입 다음 ,쉼표를 쓰고 띄어쓰기 후 CaseIterable채택
enum School2:String, CaseIterable {
    case primary = "유치원"
    case elementary = "초등학교"
    case middle = "중학교"
    case high = "고등학교"
    case college = "대학"
    case university = "대학교"
    case graduate = "대학원"
}

let allCases2:[School2] = School2.allCases
print(allCases2)

// 조금 복잡해지는 열거형은 쉽게 사용하기 어렵다 => 플랫폼 별 사용조건 추가시..
enum School3:String, CaseIterable {
    case primary = "유치원"
    case elementary = "초등학교"
    case middle = "중학교"
    case high = "고등학교"
    case college = "대학"
    case university = "대학교"
    @available(iOS, obsoleted:12.0)
    case graduate = "대학원"
    
    // 케이스가 나뉘는 경우는 allCases 프로퍼티를 구현해주어야 한다.
    static var allCases:[School3]{
        let all:[School3] = [.primary,.elementary,.middle,.high,.college,.university]
        
        #if os(iOS)
        return all
        #else
        return all + [.graduate]
        #endif
    }
}

let allCases3:[School3] = School3.allCases


// 연관 값을 갖는 열거형의 항목 순회

enum PastaTaste: CaseIterable{
    case cream,tomato
}

enum PizzaDough: CaseIterable{
    case cheeseCrust, thin, original
}

enum PizzaToping:CaseIterable{
    case pepperoni, cheese, bacon
}

enum MainDish: CaseIterable {
    case pasta(taste:PastaTaste)
    case pizza(dough:PizzaDough,topping:PizzaToping)
    case chicken(withSauce:Bool)
    case rice
    
    static var allCases: [MainDish]{
        return PastaTaste.allCases.map(MainDish.pasta)
            + PizzaDough.allCases.reduce([]){
                (result,dough) ->[MainDish] in result + PizzaToping.allCases.map{(topping) -> MainDish in MainDish.pizza(dough: dough, topping: topping)
                }
        }
            + [true, false].map(MainDish.chicken)
            + [MainDish.rice]
    }
}

print(MainDish.allCases.count)
print(MainDish.allCases)
//: [Next](@next)


