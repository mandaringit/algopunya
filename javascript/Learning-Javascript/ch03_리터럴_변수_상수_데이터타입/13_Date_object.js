// 자바스크립트 Date 객체는 자바에서 가져온거다.
// 사용하기 어려운 편. 타임존이 다른 날짜를 다룰 때는 매우 어렵다.

// 날짜 객체를 만들자.
const now = new Date();
console.log(now);

// 특정 날짜에 해당하는 객체를 만들자.
const halloween = new Date(2016,9,31);
console.log(halloween);

// 특정 날짜 및 시간에 해당하는 객체를 만들자.
const halloweenParty = new Date(2016,9,31,19,0);
console.log(halloweenParty);

// 각 파트를 가져올 수 있다.
console.log(halloweenParty.getFullYear());
console.log(halloweenParty.getMonth());
console.log(halloweenParty.getDate());
console.log(halloweenParty.getDay()); // 1 : 월요일, 0 => 일요일
console.log(halloweenParty.getHours());
console.log(halloweenParty.getMinutes());
console.log(halloweenParty.getSeconds());
console.log(halloweenParty.getMilliseconds());