function sum(arr, f) {
  if (typeof f != "function") {
    f = x => x;
  }
  return arr.reduce((total, x) => total += f(x), 0);
}

// 배열과 함수를 받는 함수로는 만족스러운 결과를 얻을 수 없고,
// 배열 하나만 받아서 제곱의 합을 반환하는 함수가 필요하다.

// 이미 만들어둔 sum함수 활용
// function sumOfSquares(arr) {
//   return sum(arr, x => x * x);
// }

// 이런 패턴이 계속된다면..
// 필요한 함수를 반환하는 함수를 만들어 문제를 해결
function newSummer(f) {
  return arr => sum(arr, f)
}

// 새 함수 newSummer는 단 하나의 매개변수만 받으면서
// 원하는 중간함수를 마음대로 쓰는게 가능.

const sumOfSquares = newSummer(x => x * x);
const sumOfCubes = newSummer(x => Math.pow(x, 3));
console.log(sumOfSquares([1, 2, 3]));
console.log(sumOfCubes([1, 2, 3]));

