//: [Previous](@previous)

import Foundation

/*
 struct 구조체 이름 {
    프로퍼티와 메서드들
 }
 */

struct BasicInformation {
    var name: String
    var age: Int
}

var mandarinInfo:BasicInformation = BasicInformation(name:"mandarin",age:25)
mandarinInfo.age = 100
mandarinInfo.name = "Seba"

let sebaInfo: BasicInformation = BasicInformation(name:"Seba",age:99)
//sebaInfo.age = 100


//: [Next](@next)
