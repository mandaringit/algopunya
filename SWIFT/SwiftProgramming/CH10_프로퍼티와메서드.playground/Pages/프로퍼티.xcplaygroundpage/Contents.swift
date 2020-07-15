//: [Previous](@previous)

import Foundation

// 좌표
//struct CoordinatePoint {
//    var x: Int // 저장 프로퍼티
//    var y: Int // 저장 프로퍼티
//}
//
//// 구조체에는 기본적으로 저장 프로퍼티를 매개변수로 갖는 이니셜라이저가 존재한다.
//let mandarinPoint:CoordinatePoint = CoordinatePoint(x:10,y:5)
//
//
//// 사람의 위치정보
//class Position{
//    var point: CoordinatePoint
//    // 저장 프로퍼티 (변수) - 위치(point)는 변경될 수 있음을 뜻한다.
//    let name: String // 저장 프로퍼티 (상수)
//
//    // 프로퍼티 기본값을 지정해주지 않는다면 이니셜라이저를 따로 정의해주어야 한다.
//    init(name:String, currentPoint:CoordinatePoint){
//        self.name = name
//        self.point = currentPoint
//    }
//}
//
//// 사용자 정의 이니셜라이저를 호출해야만 합니다.
//// 그렇지 않으면 프로퍼티 초깃값을 할당할 수 없어 인스턴스 생성이 불가함.
//let mandarinPosition:Position = Position(name:"mandairn",currentPoint:mandarinPoint)

//struct CoordinatePoint {
//    var x:Int = 0
//    var y:Int = 0
//}
//
//let mandarinPoint:CoordinatePoint = CoordinatePoint()
//
//let wizplanPoint:CoordinatePoint = CoordinatePoint(x:10,y:5)
//
//print("mandarin's point: \(mandarinPoint.x), \(mandarinPoint.y)")
//print("wizplan's point: \(wizplanPoint.x), \(wizplanPoint.y)")
//
//class Position {
//    var point:CoordinatePoint = CoordinatePoint()
//    var name: String = "Unknown"
//}
//
//let mandarinPosition: Position = Position()
//
//mandarinPosition.point = mandarinPoint
//mandarinPosition.name="mandarin"

//struct CoordinatePoint {
//    // 위치는 x,y 모두 존재해야하므로 옵셔널이면 안된다.
//    var x: Int
//    var y: Int
//}
//
//class Position {
//    // 현재 사람의 위치를 모를 수도 있다. - 옵셔널
//    var point:CoordinatePoint?
//    let name:String
//
//    init(name:String){
//        self.name = name
//    }
//}
//
//// 이름은 필수인데, 위치는 모를 수 있다.
//let mandarinPosition:Position = Position(name:"mandarin")
//// 위치를 알게되면 그 때 위치 값을 할당.
//mandarinPosition.point = CoordinatePoint(x:20,y:10)
//

//struct CoordinatePoint {
//    var x: Int = 0
//    var y: Int = 0
//}
//
//class Position {
//    lazy var point: CoordinatePoint = CoordinatePoint()
//    let name :String
//
//    init(name:String){
//        self.name = name
//    }
//}
//
//let mandarinPosition:Position = Position(name: "mandarin")
//print(mandarinPosition.point)

//struct CoordinatePoint {
//    var x: Int
//    var y: Int
//
//    // 대칭점을 구하는 메서드 - 접근자
//    // Self는 타입 자기 자신을 뜻한다.
//    // Self 대신 CoordinatePoint를 써도 된다.
//    func oppositePoint() -> Self {
//        return CoordinatePoint(x:-x,y:-y)
//    }
//
//    // 대칭점을 설정하는 메서드 - 설정자
//    mutating func setOppositePoint(_ opposite:CoordinatePoint){
//        x = -opposite.x
//        y = -opposite.y
//    }
//}
//
//var mandarinPosition:CoordinatePoint = CoordinatePoint(x:10,y:20)
//// 현재 좌표
//print(mandarinPosition) // 10, 20
//
//// 대칭좌표
//print(mandarinPosition.oppositePoint())
//
//mandarinPosition.setOppositePoint(CoordinatePoint(x:15,y:10))
//print(mandarinPosition)
//
//struct CoordinatePoint {
//    var x: Int
//    var y: Int
//
//    // 대칭좌표
//    var oppositePoint: CoordinatePoint{
//        // 접근자
//        get {
//            return CoordinatePoint(x:-x,y:-y)
//        }
//
//    }
//}
//
//var mandarinPostion:CoordinatePoint = CoordinatePoint(x: 10, y: 20)
//
//print(mandarinPostion)
//print(mandarinPostion.oppositePoint)
//// 설정자 구현 없으므로 오류.
//mandarinPostion.oppositePoint = CoordinatePoint(x: 15, y: 10)


//class Account {
//    var credit:Int = 0 {
//        willSet {
//            print("잔액이 \(credit)원에서 \(newValue)원으로 변경될 예정입니다.")
//        }
//
//        didSet{
//            print("잔액이 \(oldValue)원에서 \(credit)원으로 변경되었습니다.")
//        }
//    }
//
//    var dollarValue:Double { // 연산 프로퍼티
//        get {
//            return Double(credit) / 1000.0
//        }
//
//        set {
//            credit = Int(newValue * 1000)
//            print("잔액을 \(newValue)달러로 변경중입니다.")
//        }
//    }
//}
//
//class ForeignAccount: Account {
//    override var dollarValue: Double{
//        willSet {
//            print("잔액이 \(dollarValue)달러에서 \(newValue)달러로 변경될 예정입니다.")
//        }
//
//        didSet{
//            print("잔액이 \(oldValue)달러에서 \(dollarValue)달러로 변경되었습니다.")
//        }
//    }
//}
//
//let myAccount: ForeignAccount = ForeignAccount()
//
//myAccount.credit = 1000
//
//myAccount.dollarValue = 2
//
//
//var wonInPocket:Int = 2000 {
//    willSet {
//        print("주머니의 돈이 \(wonInPocket)원에서 \(newValue)원으로 변경될 예정입니다.")
//    }
//
//    didSet {
//        print("주머니의 돈이 \(oldValue)원에서 \(wonInPocket)원으로 변경되었습니다.")
//    }
//}
//
//var dollarInPocket:Double {
//    get {
//        return Double(wonInPocket) / 1000.0
//    }
//
//    set {
//        wonInPocket = Int(newValue * 1000.0)
//        print("주머니의 달러를 \(newValue)달러로 변경 중입니다.")
//    }
//}
//
//dollarInPocket = 3.5
//
//// 타입 프로퍼티
//
//class AClass {
//
//    // 저장 타입 프로퍼티
//    static var typeProperty:Int = 0
//
//    // 저장 인스턴스 프로퍼티
//    var instanceProperty:Int = 0{
//        didSet{
//            // Self.typeProperty는
//            // AClass.typeProperty와 같은 표현.
//            Self.typeProperty = instanceProperty + 100
//        }
//    }
//
//    // 연산 타입 프로퍼티
//    static var typeComputedProperty:Int {
//        get {
//            return typeProperty
//        }
//
//        set {
//            typeProperty = newValue
//        }
//    }
//}

//AClass.typeProperty = 123
//let classInstance:AClass = AClass()
//classInstance.instanceProperty = 100
//
//print(AClass.typeProperty)
//print(AClass.typeComputedProperty)

class Account{
    static let dollarExchangeRate:Double = 1000.0
    
    var credit:Int = 0 // 저장 인스턴스 프로퍼티
    
    var dollarValue:Double { // 연산 인스턴스 프로퍼티
        get {
            return Double(credit) / Self.dollarExchangeRate
        }
        set {
            credit = Int(newValue * Account.dollarExchangeRate)
            print("잔액을 \(newValue)달러로 변경 중입니다.")
        }
    }
    
}

class Person {
    let name: String
    
    init(name:String){
        self.name = name
    }
}

struct Stuff {
    var name: String
    var owner: Person
}

let mandarin = Person(name:"madnarin")
let hana = Person(name: "hana")
let macbook = Stuff(name: "MacBook Pro", owner: mandarin)
var iMac = Stuff(name:"iMac",owner: mandarin)
let iPhone = Stuff(name: "iPhone", owner: hana)

let stuffNameKeyPath = \Stuff.name
let ownerkeyPath = \Stuff.owner

// \Stuff.owner.name과 같은 의미이다.
let ownerNameKeyPath = ownerkeyPath.appending(path: \.name)

// 키 경로와 서브스크립트를 이용해 프로퍼티에 접근하려 값을 가져온다.
print(macbook[keyPath:stuffNameKeyPath])
print(iMac[keyPath:stuffNameKeyPath])
print(iPhone[keyPath:stuffNameKeyPath])

print(macbook[keyPath:ownerNameKeyPath])
print(iMac[keyPath:ownerNameKeyPath])
print(iPhone[keyPath:ownerNameKeyPath])

// 키 경로와 서브스크립트를 이용해 프로퍼티에 접근하여 값을 변경
iMac[keyPath:stuffNameKeyPath] = "iMac Pro"
iMac[keyPath:ownerkeyPath] = hana

print(iMac[keyPath:stuffNameKeyPath])
print(iMac[keyPath:ownerNameKeyPath])


// 상수로 지정한 값 타입과 읽기 전용 프로퍼티는
// 키 경로 서브스크립트로도 값을 바꿔줄 수 없다.
// macbook[keyPath:stuffNameKeyPath] = "macbook pro touch bar"
// mandarin[keyPath:\Person.name] = "bear"



//: [Next](@next)
