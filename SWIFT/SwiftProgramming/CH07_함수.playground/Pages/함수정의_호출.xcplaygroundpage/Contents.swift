//: [Previous](@previous)

import Foundation

// 매개변수 타입이 다르다 => 같은 이름의 함수를 여러개 만들 수 있다.
// 매개변수의 개수가 달라도 같은 이름의 함수를 만들 수 있다.

/*
 
 func 함수 이름 (매개변수...) -> 반환 타입 {
    실행 구문
    return 반환 값
 }
 
 */

func hello(name:String) -> String {
    return "Hello \(name)!"
}

let helloJenny:String = hello(name:"Jenny")
print(helloJenny)

// 리턴 키워드 생략. - 함수 내부의 코드가 한줄, 표현이 결괏값 타입과 일치시.
func introduce(name:String) -> String {
    "제 이름은" + name + "입니다."
}

let introduceJenny:String = introduce(name:"Jenny")
print(introduceJenny)

// 1. 매개변수가 없는 함수
func helloWorld() -> String {
    return "Hello, world"
}
print(helloWorld())

// 2. 매개변수가 여러 개인 함수
func sayHello(myName:String,yourName:String) -> String {
    return "Hello \(yourName)! I'm \(myName)"
}
// 주의할 점은, 함수 호출 시 매개변수 이름을 붙여주고 콜론을 적고 전달 인자를 보내준다.
print(sayHello(myName:"mandarin",yourName:"Jenny"))

// 3. 매개변수 이름과 전달인자 레이블
// 위에서 myName, yourName => 매개변수 이름
// 전달인자 레이블
/*
 func 함수 이름 (전달인자레이블 매개변수이름 : 매개변수타입, 전달인자레이블 매개변수이름: 매개변수타입 ... ) -> 반환타입 {
    실행 구문
    return 반환 값
 }
 */

func sayHello(from myName:String,to name:String) -> String {
    return "Hello \(name)! I'm \(myName)"
}

print(sayHello(from:"mandarin",to:"Jenny"))

// 전달인자 레이블이 없는 함수 정의 및 사용
func sayHello(_ name:String,_ times:Int) -> String {
    var result :String = ""
    
    for _ in 0..<times {
        result += "Hello \(name)" + " "
    }
    
    return result
}

print(sayHello("chope",2))


func sayHello(to name:String, _ times: Int) -> String {
    var result:String  = ""
    
    for _ in 0..<times {
        result += "Hello \(name)" + " "
    }
    
    return result
}

func sayHello(to name:String, repeatCount times:Int) -> String {
    var result:String  = ""
    
    for _ in 0..<times {
        result += "Hello \(name)" + " "
    }
    
    return result
}

// 전달 인자 레이블만 다르게 써주면 함수 중복 정의 가능(오버로드)
print(sayHello(to:"Chope",2))
print(sayHello(to:"Chope",repeatCount:2))

// 매개변수 기본값
func sayHello(_ name:String, times:Int = 3) -> String {
    var result:String = ""
    
    for _ in 0..<times {
        result += "Hello \(name)!" + " "
    }
    
    return result
}

print(sayHello("Hana"))
print(sayHello("Joe",2))


// 가면 매개변수와 입출력 매개변수
func sayHelloToFriends(me:String, friends names:String...) -> String{
    var result:String = ""
    
    for friend in names{
        result += "Hello \(friend)!" + " "
    }
    
    result += "I'm " + me + "!"
    return result
}

print(sayHelloToFriends(me:"mandarin", friends:"Jenny","Jay","Joe"))
print(sayHelloToFriends(me:"mandarin"))

// 참조는 inout 매개변수로 전달될 변수 또는 상수 앞에 앰퍼샌드(&)를 붙여 표현한다.

var numbers:[Int] = [1,2,3]
func nonReferneceParameter(_ arr:[Int]) {
    var copiedArr:[Int] = arr
    copiedArr[1] = 1
    print(copiedArr)
}

func referenceParameter(_ arr: inout [Int]){
    arr[1] = 1
}

print(numbers)
nonReferneceParameter(numbers)
print(numbers[1])
referenceParameter(&numbers)
print(numbers[1])
// 메모리 안전 위협도 있음.

// 반환값이 굳이 필요 없는 경우도 있다. Void 또는 표현 생략.
func sayHelloWorld(){
    print("Hello, world!")
}
sayHelloWorld()

func sayHello2(from myName: String, to name: String) {
    print("Hello \(name)! I'm \(myName)")
}

sayHello2(from:"mandarin", to:"Mijeong")

func sayGoodbye() -> Void {
    print("Good bye")
}
sayGoodbye()

// 데이터 타입으로서의 함수
/*
 (매개변수 타입의 나열) -> 반환 타입
 */

typealias CalculateTwoInts = (Int,Int) -> Int

func addTwoInts(_ a:Int,_ b:Int) -> Int {
    return a+b
}

func multiplyTwoInts(_ a:Int, _ b:Int) -> Int {
    return a*b
}

var mathFunction: CalculateTwoInts = addTwoInts
// var mathFunction:(Int,Int) -> Int = addTwoInts 와 동일한 표현
print(mathFunction(2,5))

mathFunction = multiplyTwoInts
print(mathFunction(2,5))

// 전달 인자로 함수 사용
func printMathResult(_ mathFn:CalculateTwoInts, _ a:Int,_ b:Int) {
    print("Result: \(mathFn(a,b))")
}
printMathResult(addTwoInts, 3, 5)

// 반환 값으로 함수 반환
func chooseMathFunction(_ toAdd:Bool) -> CalculateTwoInts {
    return toAdd ? addTwoInts : multiplyTwoInts
}

printMathResult(chooseMathFunction(true), 3, 5)

//: [Next](@next)
