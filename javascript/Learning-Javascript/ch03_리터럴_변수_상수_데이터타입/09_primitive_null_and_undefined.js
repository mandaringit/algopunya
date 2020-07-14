// null과 undefined는 자바스크립트의 특별한 타입이다.
// 둘 다 자기자신 하나밖에 못가진다.
// 모두 존재하지 않는 것을 나타낸다.

// null => 프로그래머에게 허용된 데이터 타입 => 변수의 값을 아직 모르거나 적용할 수 없는 경우는 대부분 null.
// undefined => 자바스크립트 자체에서 사용한다.

let currentTemp; // 암시적으로 undefined
console.log(currentTemp);

const targetTemp = null; // "아직 모르는 값"
console.log(targetTemp);

currentTemp = 19.5; // 할당
console.log(currentTemp);

currentTemp = undefined; // 초기화 시키지 않은듯 하다. 권장하지 않음.
console.log(currentTemp);