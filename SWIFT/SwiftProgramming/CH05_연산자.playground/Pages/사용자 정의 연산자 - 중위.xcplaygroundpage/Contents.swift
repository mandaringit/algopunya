//: [Previous](@previous)

import Foundation

// ###### 사용자 정의 중위 연산자 ######

/*
precedencegroup 우선순위 그룹 이름 {
    higerThan: 더 낮은 우선순위 그룹 이름
    lowerThan: 더 높은 우선순위 그룹 이름
    associativity: 결합 방향 (left,right,none)
    assignment: 할당 방향 사용 (true,false)
}
*/


// MultiplicationPrecedence 명시 안하면 DefaultPrecedence 그룹으로
// 자동지정됩니다.
infix operator ** : MultiplicationPrecedence

func ** (lhs:String,rhs:String) -> Bool {
    return lhs.contains(rhs)
}

let hellomandarin:String = "Hello mandarin"
let mandarin: String = "mandarin"
let isContainsMandarin:Bool = hellomandarin ** mandarin

// 우리가 정의한 데이터타입(클래스, 구조체) 등에서 유용하게 사용할 수 있는 연산자도 새로 정의하거나 중복 정의 가능함을 알 수 있다.

class Car {
    var modelYeaer:Int?
    var modelName:String?
}

struct SmartPhone {
    var company:String?
    var model:String?
}

// 모델 네임이 같으면 true
func == (lhs:Car,rhs:Car) -> Bool {
    return lhs.modelName == rhs.modelName
}

func == (lhs:SmartPhone,rhs:SmartPhone) -> Bool {
    return lhs.model == rhs.model
}

let myCar = Car()
myCar.modelName = "S"
let yourCar = Car()
yourCar.modelName = "S"

var myPhone = SmartPhone()
myPhone.model = "SE"
var yourPhone = SmartPhone()
yourPhone.model = "XS"

print(myCar == yourCar)
print(myPhone == yourPhone)

// 전역에 선언하긴 했지만, 특정 타입에 국한된 연산자는 타입 내부에 구현하는게 올바를것.

class Car2 {
    var modelYeaer:Int?
    var modelName:String?
    
    static func == (lhs:Car2,rhs:Car2) -> Bool {
        return lhs.modelName == rhs.modelName
    }
}


struct SmartPhone2 {
    var company:String?
    var model:String?
    
    static func == (lhs:SmartPhone2,rhs:SmartPhone2) -> Bool {
        return lhs.model == rhs.model
    }

}

// 이는 강력한 무기가 될 수 있다!

//: [Next](@next)
