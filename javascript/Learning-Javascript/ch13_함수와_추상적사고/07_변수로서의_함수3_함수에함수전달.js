function sum(arr, f) {
  // 함수가 전달되지 않았으면 매개변수를 그대로 반환하는 null함수를 쓴다.
  if (typeof f != "function") {
    f = x => x; // 원래대로 반환하는 함수
  }
  return arr.reduce((total, x) => total += f(x), 0);
}

console.log(sum([1, 2, 3]));
console.log(sum([1, 2, 3], x => x * x));
console.log(sum([1, 2, 3], x => Math.pow(x, 3)));
