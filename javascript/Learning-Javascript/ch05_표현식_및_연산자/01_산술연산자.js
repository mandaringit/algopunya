// 단항 부정 이후 뺄셈
const x = 5;
const y = 3 - -x;
console.log(y); // 8

// 단항 플러스 (형변환기능)
const s = '5'; // 문자열 5
const z = 3 + +s;
console.log(z); // number 8

// 단순 줄맞추기 용도
const x1 = 0, x2 = 3, x3 = -1.5, x4 = -6.33;
const p1 = -x1 * 1;
const p2 = +x2 * 2;
const p3 = +x3 * 3;
const p4 = -x4 * 4;
console.log(p1, p2, p3, p4);

// x % y 연산자 => 피제수(x)를 제수(y)로 나눈 나머지.
const a = 10;
const b = 3;
console.log(a % b);

// 전위, 후위 연산자. 표현식 깊숙이 묻혀 있으면 부작용을 주의해야한다.

// 전위 연산자 -> 먼저 변수의 값을 바꾼 다음 평가한다.
// 후위 연산자 -> 값을 바꾸기 전에 평가한다.
let k = 2;
const r1 = k++ + k++; // k=2 에서 시작, (k=2) + (k=3) = 5  계산이 끝난 단계에서 k=5.
const r2 = ++k + ++k; // k=5 에서 시작, (k=5) + (k=6) = 11
const r3 = k++ + ++k; // k=6에서 시작, (k=6) + (k=8) = 14
const r4 = ++k + k++; // k=8에서 시작, (k=9) + (k=9) = 18 계산 이후 k=10
console.log(r1, r2, r3, r4, k);

let m = 10;
const r5 = m-- + m--; // m=10에서 시작, (m=10) + (m=9) = 19 계산이 끝난 단계에서 m=8
const r6 = --m + --m; // m=8에서 시작, (m=7) + (m=6) = 13
const r7 = m-- + --m; // m=6에서 시작, (m=6) + (m=4) = 10
const r8 = --m + m--; // m=4에서 시작, (m=3) + (m=3) = 6 계산이 끝난 단계에서 m=2
console.log(r5, r6, r7, r8, m);
