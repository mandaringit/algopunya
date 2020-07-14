// 5장을 주로 참고.

// !(부정연산자)를 사용해 모든 값을 불리언으로 변경 가능하다.
const n = 0; // 거짓 같은 값
const b = !n; // 부정 false -> true
const b1 = !!n; // 이중 부정 false -> true -> false
const b2 = Boolean(n); // new 키워드는 쓰지 않습니다.
console.log(n, b, b1, b2);

