//: [Previous](@previous)

import Foundation

// 튜플은 타입의 이름이 따로 지정되어 있지 않고, 프로그래머 마음대로 만드는 타입이다.
// "지정된 데이터의 묶음" 이라고 표현 가능하다. => C언어의 원시 구조체 형태와 비슷
// 포함될 갯수는 여러개 가능.

//String, Int, Double 타입을 갖는 튜플
var person: (String,Int,Double) = ("mandarin",100,182.5)

// 인덱스를 통해 값을 빼올 수 있다.
print("이름 :\(person.0), 나이: \(person.1), 신장: \(person.2)")

person.1 = 99
person.2 = 178.5

print("이름 : \(person.0), 나이 : \(person.1), 신장 : \(person.2)")

// 이름없이 인덱스만으론 각 요소의 데이터가 무엇인지 파악하기 어렵다. => 이름을 붙이자
// String, Int, Double 타입을 갖는 튜플
var person2:(name:String,age:Int,height:Double) = ("mandarin",100,182.5)

// 요소 이름을 통해서 값을 빼 올 수 있다.
print("이름 : \(person2.name), 나이 : \(person2.age), 신장 : \(person2.height)")

person2.age = 99
person2.2 = 178.5

print("이름: \(person2.0), 나이:\(person2.1), 신장:\(person2.2)")

// 튜플은 타입 이름에 해당하는 키워드가 따로 없다보니 사용에 불편함을 겪기도 한다.
// 매번 같은 모양의 튜플을 사용하고 싶은데 선언해줄 때마다 긴 튜플 타입을 모두 써줘야 하는 불편함이 생길 수 있기 때문이다.
// 이럴 때 typealias를 쓴다.
typealias PersonTuple = (name:String,age:Int,height:Double)

let mandarin:PersonTuple = ("mandarin",100,178.5)
let jun:PersonTuple = ("Jun",100,155)

print("이름:\(mandarin.name), 나이:\(mandarin.age), 키:\(mandarin.height)")
print("이름:\(jun.name), 나이:\(jun.age), 키:\(jun.height)")


//: [Next](@next)
