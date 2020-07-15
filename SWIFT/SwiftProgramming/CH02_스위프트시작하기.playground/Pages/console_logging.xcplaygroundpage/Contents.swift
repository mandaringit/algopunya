//: [Previous](@previous)

import Foundation

var str = "Hello, playground"
var j = 1
for i in 0...3 {
    j += i
}

print("Hello World!")

struct BasicInformation {
    let name: String
    var age: Int
}

var yagomInfo: BasicInformation = BasicInformation(name:"yagom",age:99)

class Person {
    var height:Float = 0.0
    var weight:Float = 0.0
}

let yagom: Person = Person()
yagom.height = 182.5
yagom.weight = 78.5

print(yagomInfo)
dump(yagomInfo)
print(yagom)
dump(yagomInfo)

// 문자열 보간법
let name: String = "yagom"
print("My name is \(name)")

//: [Next](@next)
