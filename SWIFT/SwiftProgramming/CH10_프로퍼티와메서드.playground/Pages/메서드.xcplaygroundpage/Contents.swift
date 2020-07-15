//: [Previous](@previous)

import Foundation

//class LevelClass {
//    // 현재 레벨 저장하는 저장 프로퍼티
//    var level: Int = 0 {
//        didSet {
//            print("Level \(level)")
//        }
//    }
//
//    func levelUp() {
//        print("Level Up!")
//        level += 1
//    }
//
//    func levelDown(){
//        print("Level Down")
//        level -= 1
//        if level < 0 {
//            reset()
//        }
//    }
//
//    func jumpLevel(to:Int){
//        print("Jump to \(to)")
//        level = to
//    }
//
//    func reset() {
//        print("Reset!")
//        level = 0
//    }
//}
//
//var levelClassInstance:LevelClass = LevelClass()
//levelClassInstance.levelUp()
//levelClassInstance.levelDown()
//levelClassInstance.levelDown()
//levelClassInstance.jumpLevel(to:3)

//struct LevelClass {
//    // 현재 레벨 저장하는 저장 프로퍼티
//    var level: Int = 0 {
//        didSet {
//            print("Level \(level)")
//        }
//    }
//
//    mutating func levelUp() {
//        print("Level Up!")
//        level += 1
//    }
//
//    mutating func levelDown(){
//        print("Level Down")
//        level -= 1
//        if level < 0 {
//            reset()
//        }
//    }
//
//    mutating func jumpLevel(to:Int){
//        print("Jump to \(to)")
//        level = to
//    }
//
//    mutating func reset() {
//        print("Reset!")
//        level = 0
//    }
//}
//
//var levelClassInstance:LevelClass = LevelClass()
//levelClassInstance.levelUp()
//levelClassInstance.levelDown()
//levelClassInstance.levelDown()
//levelClassInstance.jumpLevel(to:3)

//class LevelClass {
//    var level:Int = 0
//
//    func jumpLevel(to level:Int){
//        print("Jump to \(level)")
//        self.level = level
//    }
//}

//class LevelClass {
//    var level:Int = 0
//
//    func reset(){
//        // 오류. self 프로퍼티 참조 변경 불가
//        self = LevelClass()
//    }
//}

struct LevelStruct {
    var level:Int = 0
    
    mutating func levelUp(){
        print("Level Up!")
        level += 1
    }
    
    mutating func reset(){
        print("Reset!")
        self = LevelStruct()
    }
}

var levelStructInstance: LevelStruct = LevelStruct()
levelStructInstance.levelUp()
print(levelStructInstance.level)

levelStructInstance.reset()
print(levelStructInstance.level)

enum OnOffSwitch {
    case on,off
    mutating func nextState() {
        self = self == .on ? .off :.on
    }
}

var toggle:OnOffSwitch = OnOffSwitch.off
toggle.nextState()
print(toggle)

class AClass {
    static func staticTypeMethod() {
        print("AClass staticTypeMethod")
    }
    
    class func classTypeMethod() {
        print("AClass classTypeMethod")
    }
}

class BClass:AClass {
    /*
     // 오류 발생. 재정의 불가.
    override static func staticTypeMethod () {
        
    }
     */
    
    override class func classTypeMethod() {
        print("BClass classTypeMethod")
    }
}

AClass.staticTypeMethod()
AClass.classTypeMethod()
BClass.classTypeMethod()

// 시스템 음량은 한 기기에서 유일한 값이어야 한다.
struct SystemVolume {
    // 타입 프로퍼티를 사용하면 언제나 유일한 값이 된다.
    static var volume:Int = 5
    
    // 타입 프로퍼티를 제어하기 위해 타입 메서드를 사용
    static func mute() {
        // SystemVolume.volume = 0 과 동일.
        // Self.volume = 0 과도 동일.
        self.volume = 0
    }
}


// 내비게이션 역할은 여러 인스턴스가 수행할 수 있다.
class Navigation {
    // 인스턴스마다 음량을 따로 설정 할 수 있다.
    var volume:Int = 5
    
    // 길 안내 음성 재생
    func guideWay(){
        // 내비게이션 외 다른 재생원 음소거
        SystemVolume.mute()
    }
    
    // 길 안내 음성 종료
    func finishGuideWay() {
        // 기존 재생원 음량 복구
        SystemVolume.volume = self.volume
    }
}

SystemVolume.volume = 10
let myNavi: Navigation = Navigation()

myNavi.guideWay()
print(SystemVolume.volume)

myNavi.finishGuideWay()
print(SystemVolume.volume)

//: [Next](@next)
