// some은 조건에 맞는 요소를 찾으면 즉시 검색을 멈추고 true 반환. 찾지 못하면 false반환.
const arr = [5, 7, 12, 15, 17];
console.log(arr.some(x => x % 2 === 0));
console.log(arr.some(x => Number.isInteger(Math.sqrt(x))));

// every 는 배열의 모든 요소가 조건에 맞아야 true를 반환, 아니면 false
// every는 조건에 맞지 않는 요소를 찾아야만 검색을 멈추고 false를 반환.

const arr2 = [4, 6, 16, 36];
console.log(arr2.every(x => x % 2 === 0));
console.log(arr2.every(x => Number.isInteger(Math.sqrt(x))));

// this로 사용할 값을 두 번째 매개변수로 받을 수 있다.
console.log(arr2.every(() => Number.isInteger(Math.sqrt(this.x)), arr2));


