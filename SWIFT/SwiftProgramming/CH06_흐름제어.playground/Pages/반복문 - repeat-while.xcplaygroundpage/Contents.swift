//: [Previous](@previous)

import Foundation

// do-while 구문과 다르지 않다. repeat - while

var names:[String] = ["John","Jenny","Joe","mandarin"]

repeat {
    print("Good bye \(names.removeFirst())")
    
} while names.isEmpty == false

//: [Next](@next)
