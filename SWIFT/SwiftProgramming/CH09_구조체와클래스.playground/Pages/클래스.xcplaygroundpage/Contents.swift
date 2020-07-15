//: [Previous](@previous)

import Foundation

class Person {
    var height: Float = 0.0
    var weight: Float = 0.0
    
    deinit {
        print("Person 클래스의 인스턴스가 소멸됩니다.")
    }
}

var mandarin:Person? = Person()

mandarin = nil

let jenny: Person = Person()
jenny.height = 123.4
jenny.weight = 123.4




//: [Next](@next)
