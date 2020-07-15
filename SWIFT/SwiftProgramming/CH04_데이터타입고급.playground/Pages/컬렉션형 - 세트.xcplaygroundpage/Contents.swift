//: [Previous](@previous)

import Foundation

// 같은 타입의 데이터를 순서 없이, "중복 없이" 하나의 묶음으로 저장
// 세트의 요소로는 해시 가능한 값 => Hashable프로토콜을 따른다. => 스위프트 기본 데이터 타입은 모두 해시 가능.
// 축약형 없음
// let => 변경 불가 / var => 변경 가능

var names: Set<String> = Set<String>()
var names2:Set<String> = []

// 배열처럼 대괄호 사용
var names3:Set<String> = ["mandarin","chulsoo","uonghee","mandarin"]

// 타입추론 쓰면 Array로 타입을 지정함.(주의)
var numbers = [100,200,300]
print(type(of:numbers))

print(names3.isEmpty)
print(names3.count)

// 요소 추가: insert
print(names3.count)
names3.insert("jenny")
print(names3.count)

print(names3.remove("chulsoo"))
print(names3.remove("john"))

// 집합 관계를 표현하고자 할 때 유용하게 쓰인다.
// sorted() 메서드로 정렬된 배열 반환 가능

let englishClassStudents:Set<String> = ["john","chulsoo","mandarin"]
let koreanClassStudents:Set<String> = ["jenny","mandarin","chulsoo","hana","minsoo"]

// 교집합
let intersectSet: Set<String> = englishClassStudents.intersection(koreanClassStudents)

// 여집합의 합(배타적 논리 합)
let symmetricDiffSet:Set<String> = englishClassStudents.symmetricDifference(koreanClassStudents)

// 합집합
let unionSet: Set<String> = englishClassStudents.union(koreanClassStudents)

// 차집합
let subtractSet:Set<String> = englishClassStudents.subtracting(koreanClassStudents)

// 포함관계를 연산할 수 있는 메서드로 구현

let 새: Set<String> = ["비둘기","닭","기러기"]
let 포유류: Set<String> = ["사자","호랑이","곰"]
let 동물: Set<String> = 새.union(포유류) // 새, 포유류 합집합

print(새.isDisjoint(with:포유류)) // 서로 배타적인가?
print(새.isSubset(of:동물)) // 새가 동물의 부분집합인가?
print(동물.isSuperset(of:포유류)) // 동물은 포유류의 전체집합인가?
print(동물.isSuperset(of:새)) // 동물은 새의 전체집합인가?


//: [Next](@next)
