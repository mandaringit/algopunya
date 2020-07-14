// 자바스크립트 배열은 특수한 객체다.
// 항상 순서가 있고, 키는 순차적인 숫자다.
// 메서드도 많은 강력한 객체다.

// 자바스크립트 배열은 C의 효율적인 배열 + 강력한 동적 배열 + 링크드 리스트의 혼합이다.

// 1. 배열 크기는 고정되지 않는다. 언제든 요소 추가 제거 가능.
// 2. 요소의 데이터 타입을 가리지 않는다.
// 3. 배열 요소는 0으로 시작한다.

// 이하 다양한 구성의 배열
const a1 = [1, 2, 3, 4];
const a2 = [1, "two", 3, null];
const a3 = [
    "What the hammer? What the chain?",
    "In what furnace was thy brain?",
    "What the anvil? What dread grasp",
    "Dare its deadly terrors clasp?",
];
const a4 = [
    {name: "Ruby", hardness: 9},
    {name: "Diamond", hardness: 10},
    {name: "Topaz", hardness: 8},
];
const a5 = [
    [1, 3, 5],
    [2, 4, 6],
];

// 요소 숫자 반환
const arr = ['a', 'b', 'c'];
console.log(arr.length)

// 요소 접근
console.log(arr[0]); // 첫번째 요소
console.log(arr[arr.length - 1]); // 마지막 요소

const arr2 = [1, 2, 'c', 4, 5];
arr2[2] = 3;
console.log(arr2);