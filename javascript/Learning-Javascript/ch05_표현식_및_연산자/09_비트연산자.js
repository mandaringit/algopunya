// 비트 연산자는 피연산자를 2의 보수 형식으로 저장된 32비트 부호붙은 정수로 간주한다.
// 자바스크립트는 비트 연산자를 실행하기 전에 숫자를 먼저 32비트 정수로 변환한다.
// 결과를 반환할 때 다시 더블 형식으로 반환한다.

// 비트 AND
console.log((0b1010 & 0b1100).toString(2));

// 비트 OR
console.log((0b1010 | 0b1100).toString(2));

// 비트 XOR
console.log((0b1010 ^ 0b1100).toString(2));

// 비트 NOT
console.log((~0b1010).toString(2));

// 왼쪽 시프트 (2를 곱한 효과)
console.log((0b1010<<1).toString(2));
console.log((0b1010<<2).toString(2));

// 부호가 따라가는 오른쪽 시프트 (2로 나눈 다음 소수점 아래를 버림)
let n = 22;
console.log("n       : ",n.toString(2));
console.log("n >> 1  : ",(n>>1).toString(2));
console.log("n >>> 1 : ",(n>>>1).toString(2));
console.log("n = ~n  : ",(~n).toString(2));
console.log("n++     : ",(n++).toString(2));

// 하드웨어를 직접 다루거나 하지 않는다면 크게 쓸일이 없긴 하다...