//: [Previous](@previous)

import Foundation

// 열거형 내의 항목(case)이 자신과 연관된 값을 가질 수 있다.
// 각 항목 옆에 소괄호로 묶어 표현 가능

enum MainDish {
    case pasta(taste:String)
    case pizza(dough:String,topping:String)
    case chicken(withSauce:Bool)
    case rice
}

var dinner:MainDish = MainDish.pasta(taste: "크림")
dinner = .pizza(dough: "치즈 크러스트", topping: "불고기")
dinner = .chicken(withSauce: true)
dinner = .rice

// 열거형 응용

enum PastaTaste{
    case cream,tomato
}

enum PizzaDough {
    case cheeseCrust,thin,original
}

enum PizzaToping {
    case pepperoni,cheese,bacon
}

enum MainDish2 {
    case pasta(taste:PastaTaste)
    case pizza(dough:PizzaDough,topping:PizzaToping)
    case chicken(withSauce:Bool)
    case rice
}

var dinner2:MainDish2 = MainDish2.pasta(taste:  PastaTaste.tomato)
dinner2 = MainDish2.pizza(dough: PizzaDough.cheeseCrust, topping: PizzaToping.bacon)


//: [Next](@next)
