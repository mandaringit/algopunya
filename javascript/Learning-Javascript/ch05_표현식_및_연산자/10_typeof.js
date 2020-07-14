// typeof 연산자는 피연산자의 타입을 나타내는 문자열을 반환한다.

// typeof 연산자는 일곱가지 데이터 타입을 정확히 나타내지 못한다..!
// null은 객체가 아니라 당연히 원시값이지만,
console.log(typeof null); // object 를 반환한다.

// 배열과 배열 아닌 객체도 정확히 구분 못함.
// 함수는 식별함.

// typeof 는 연산자이기 때문에 괄호는 필요없다.

console.log(typeof []); // object
console.log(typeof undefined);
console.log(typeof null);
console.log(typeof {});
console.log(typeof true);
console.log(typeof 1);
console.log(typeof "");
console.log(typeof Symbol());
console.log(typeof function () {});

