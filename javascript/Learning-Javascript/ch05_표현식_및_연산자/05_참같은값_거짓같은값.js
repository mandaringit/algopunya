// 거짓같은 값
const f1 = undefined;
const f2 = null;
const f3 = false;
const f4 = 0;
const f5 = NaN;
const f6 = '';

// 이외에는 모두 참 같은 값이다.
// 1. 모든 객체.  객체를 원시값으로 변환하는 valueOf() 메서드를 호출 했을때 false를 반환하는 객체도 참 같은 값에 속한다.
// 2. 배열, **빈 배열도 참 같은 값에 속한다.
console.log(Boolean([]));
// 3. 공백만 있는 문자열 (" ") 등
console.log(Boolean(" "));
// 4. 문자열 'false'
console.log(Boolean('false'));
