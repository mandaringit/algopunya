//: [Previous](@previous)

import Foundation

// 반복문이 중첩될때, 반복문을 제어하는 키워드 (break, continue)가 어떤 범위에 적용되어야 하는지 애매하거나,
// 큰 범위의 반복문을 종료하고 싶은데 작은 범위의 반복문만 종료되는 등 예상치 못한 실수를 할 수도 있습니다.

var numbers: [Int] = [3,2342,6,3252]

numbersLoop: for num in numbers{
    if num > 5 || num < 1 {
        continue numbersLoop
    }
    
    var count:Int = 0
    
    printLoop: while true {
        
        print(num)
        count += 1
        
        if count == num {
            break printLoop
        }
    }
    
    removeLoop:while true {
        if numbers.first != num {
            break numbersLoop
        }
        numbers.removeFirst()
    }
}

//: [Next](@next)
