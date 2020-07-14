// slice - 배열 일부만 가져오기.  (시작, 끝) 끝 전까지만 가져옴. 자른부분 반환.
const arr3 = [1, 2, 3, 4, 5];
let s1 = arr3.slice(3); // 3 ~
console.log(s1, arr3);
let s2 = arr3.slice(2, 4); // 2 ~ 3 번째
console.log(s2, arr3);
let s3 = arr3.slice(-2); // -2 ~ -1 번째
console.log(s3, arr3);
let s4 = arr3.slice(-2, -1); // -2 번째
console.log(s4, arr3);