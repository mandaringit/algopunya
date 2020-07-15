//: [Previous](@previous)

import Foundation

struct BasicInformation {
    let name:String
    var age :Int
}

var mandarinInfo: BasicInformation = BasicInformation(name:"mandarin",age:99)

mandarinInfo.age = 100

// mandarinInfo의 값을 복사해 할당한다.
var friendInfo:BasicInformation = mandarinInfo

print("mandarin's age: \(mandarinInfo.age)")
print("friend's age: \(friendInfo.age)")

friendInfo.age = 999

print("mandarin's age: \(mandarinInfo.age)")
print("friend's age: \(friendInfo.age)")

class Person {
    var height:Float = 0.0
    var weight:Float = 0.0
}

var mandarin:Person = Person()
var friend:Person = mandarin // mandarin의 참조를 할당.

print("mandarin's height: \(mandarin.height)")
print("friend's height: \(friend.height)")

friend.height = 185.5
// 같은곳을 참조하므로 같이 변화한다.
print("friend's height: \(friend.height)")
print("mandarin's height: \(mandarin.height)")

func changeBasicInfo(_ info: BasicInformation){
    var copiedInfo:BasicInformation = info
    copiedInfo.age = 1
}

func changePersonInfo(_ info:Person){
    info.height = 155.3
}

changeBasicInfo(mandarinInfo)
print("mandarin's age:\(mandarinInfo.age)")

changePersonInfo(mandarin)
print("mandarin's height: \(mandarin.height)")

var mandarin:Person = Person()
let friend:Person = mandarin
let anotherFriend:Person = Person()

print(mandarin === friend)
print(mandarin === anotherFriend)
print(mandarin !== anotherFriend)



//: [Next](@next)
