// Number, String, Boolean과 같은 객체에는 두가지 목적이 존재한다.
// 1. Number.INFINITY 와 같은 특별한 값을 저장한다.
// 2. 함수 형태로 기능을 제공한다.

const s = "hello";
console.log(s.toUpperCase()); // HELLO

// 자바스크립트가 "일시적인 String 객체"를 만든것이다.
// 호출 즉시 임시 객체를 파괴한다.

const s2 = "hello";
s2.rating = 3; // 마치 할당되는것 처럼 보인다. (실상은 바로 파괴)
console.log(s2.rating); // 그러나 결과는 undefined. 참고적으로만 알아두자.



