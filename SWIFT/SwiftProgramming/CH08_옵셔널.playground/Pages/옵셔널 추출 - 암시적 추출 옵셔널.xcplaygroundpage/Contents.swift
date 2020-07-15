//: [Previous](@previous)

import Foundation

var myName: String! = "mandarin"
print(myName)
myName = nil

if let name = myName {
    print("my Name is \(name)")
} else {
    print("myName == nil")
}

myName.isEmpty // 오류


//: [Next](@next)
