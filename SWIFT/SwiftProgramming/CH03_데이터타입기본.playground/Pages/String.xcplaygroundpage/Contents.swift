//: [Previous](@previous)

import Foundation

// String은 문자열의 나열 => 문자열
// 유니코드 9를 사용 할 수 있으며, 값의 앞뒤에 큰 따옴표를 사용해 표현

// 상수로 선언된 문자열은 변경불가
let name:String = "mandarin"

// 이니셜라이저를 사용해 빈 문자열 생성 가능
// var키워드로 사용하여 변수를 생성 => 변경 가능
var introduce:String = String()

// append()를 통해
introduce.append("제 이름은")

// +연산자를 통해서도 문자열을 이어붙일 수 있다.
introduce = introduce + " " + name + "입니다."

// name에 해당하는 문자의 수를 셀 수 있다.
print("name의 글자 수: \(name.count)")

// 빈 문자열인지 확인할 수 있다.
print("introduce가 비어있습니까? \(introduce.isEmpty)")

// 유니코드 스칼라값을 사용하면 값에 해당하는 표현이 출력됩니다. - 어떤 모양이 출력되는가?
let unicodeScalarValue:String = "\u{2665}"

"""
String의 다양한 기능들
"""

// 연산자를 통한 문자열 결합
let hello: String = "Hello"
let mandarin:String = "mandarin"
var greeting: String = hello + " " + mandarin + "!"
print(greeting)

greeting = hello
greeting += " "
greeting += mandarin
greeting += "!"
print(greeting)

// 연산자를 통한 문자열 비교

var isSameString:Bool = false

isSameString = hello == "Hello"
print(isSameString)

isSameString = hello == "hello"
print(isSameString)

isSameString = mandarin == "mandarin"
print(isSameString)

isSameString = mandarin == hello
print(isSameString)


// 메서드를 통한 접두어, 접미어 확인
var hasPrefix:Bool = false
hasPrefix = hello.hasPrefix("He")
print(hasPrefix)

hasPrefix = hello.hasPrefix("HE")
print(hasPrefix)

hasPrefix = greeting.hasPrefix("Hello ")
print(hasPrefix)

hasPrefix = mandarin.hasPrefix("man")
print(hasPrefix)

hasPrefix = hello.hasPrefix("Hello")
print(hasPrefix)


var hasSuffix:Bool = false
hasSuffix = hello.hasSuffix("He")

hasSuffix = hello.hasSuffix("llo")
print(hasSuffix)

hasSuffix = greeting.hasSuffix("mandarin")
print(hasSuffix)

hasSuffix = greeting.hasSuffix("mandarin!")
print(hasSuffix)

hasSuffix = mandarin.hasSuffix("rin")
print(hasSuffix)

// 메서드를 통한 대소문자 변환
var convertedString:String = ""
convertedString = hello.uppercased()
print(convertedString)

convertedString = hello.lowercased()
print(convertedString)

convertedString = mandarin.uppercased()
print(convertedString)

convertedString = mandarin.lowercased()
print(convertedString)

// 프로퍼티를 통한 빈 문자열 확인
var isEmptyString:Bool = false
isEmptyString = greeting.isEmpty
print(isEmptyString)

greeting = "안녕"
isEmptyString = greeting.isEmpty
print(isEmptyString)

greeting = ""
isEmptyString = greeting.isEmpty
print(isEmptyString)

// 프로퍼티를 이용해 문자열 길이 확인
print(greeting.count)

greeting = "안녕하세요"
print(greeting.count)

greeting = "안녕!"
print(greeting.count)

greeting = """
안녕하세요 저는 만다린입니다.
스위프트 잘하고 싶어요!
잘 부탁합니다.
"""
print(greeting.count)

//: [Next](@next)
