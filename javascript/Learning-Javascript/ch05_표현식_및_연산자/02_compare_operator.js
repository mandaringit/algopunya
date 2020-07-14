// 두 개의 값을 비교한다.

// 동등함(loose equality) -> ==
// 1. 두값이 같은 객체를 가리킨다.
// 2. 같은 값을 갖도록 변환할 수 있다 => ex) 33 == "33" -> true

// 일치함(strict equality) -> ===, !==
// 1. 두 값이 같은 객체를 가리킨다.
// 2. 같은 타입이고, 값도 같다(원시타입).
// 그냥 무조건 일치 연산자를 쓰자..

const n = 5;
const s = "5";
console.log(n === s);
console.log(n !== s);
console.log(n === Number(s));
console.log(n !== Number(s));
console.log(n == s); // true. 권장하지 않는다.
console.log(n != s); // false. 권장하지 않는다.

// 객체에 같은 정보가 들어 있어도 그들은 서로 다른 객체다. 일치x 동등x
const a = {name: "an object"};
const b = {name: "an object"};
console.log(a === b);
console.log(a !== b);
console.log(a == b); // 권장 x
console.log(a != b); // 권장 x



