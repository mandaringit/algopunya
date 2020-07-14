// 원시 값 primitive => 불변(immutable)
// 변수의 값이 바뀔 수 없다는 뜻은 아니다.

// 숫자
console.log(0.1 + 0.2);

let count = 10; // 숫자 리터럴.
const blue = 0x0000ff; // 16진수
const umask = 0o0022; // 8진수
const roomTemp = 21.5;
const c = 3.0e6;
const e = -1.6e-19;
const inf = Infinity;
const ninf = -Infinity;
const nan = NaN;

console.log(count, blue, umask, roomTemp, c, e, inf, ninf, nan);

// 숫자에 대응하는 Number 객체가 있다.
const small = Number.EPSILON;
const bigInt = Number.MAX_SAFE_INTEGER;
const max = Number.MAX_VALUE;
const minInt = Number.MIN_SAFE_INTEGER;
const min = Number.MIN_VALUE;
const ninf2 = Number.NEGATIVE_INFINITY;
const nan2 = Number.NaN;
const inf2 = Number.POSITIVE_INFINITY;

console.log(small, bigInt, max, minInt, min, ninf2, nan2, inf2);