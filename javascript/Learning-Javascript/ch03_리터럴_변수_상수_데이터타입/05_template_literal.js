let currentTemp = 19.5;

// ES6 이전엔 문자열 병합 뿐이었다.
const message = "The current temperature is " + currentTemp + "\u00b0C";
console.log(message);

// ES6 이후의 문자열 템플릿(또는 interpolation)
const message2 = `The current temperature is ${currentTemp}\u00b0C`;
console.log(message2);