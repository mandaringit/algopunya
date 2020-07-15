//: [Previous](@previous)

import Foundation

func say(_ something: String) -> String {
    print(something)
    return something
}

@discardableResult func discardableResultSay(_ something:String) -> String {
    print(something)
    return something
}

say("hello")

discardableResultSay("hello")

//: [Next](@next)
