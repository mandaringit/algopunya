// 숫자로 바꾸기

// 문자열 -> 숫자
const numStr = "33.3";
const num = Number(numStr); // Number 객체의 인스턴스가 "아닙니다." new도 붙이지 않습니다.
console.log(typeof num, num); // 못바꾸면 NaN 반환.

// 내장함수 parseInt, parseFloat 사용하기.
// parseInt는 기수(radix)를 넘길 수 있다. 기수를 명시하길 권장한다.
// 숫자로 판단 가능한 부분만 모두 변환하고 그 뒤는 전부 무시한다.
const a = parseInt("16 volts",10); // volts는 무시. 10진수 16
const b = parseInt("3a",16); // 16진수 3a를 10진수로 바꿈.
const c = parseFloat("15.5 kph");
console.log(a,b,c);

// Date 객체를 숫자로 바꿀때는 valueOf() 메서드를 사용한다. => UTC 1970-01-01 이후로부터 몇 밀리초 지났나?
const d = new Date();
const ts = d.valueOf();
console.log(`UTC 1970-01-01 이후로부터 ${ts} ms 지났습니다.`);


