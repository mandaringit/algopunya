// 프로그램을 시작할 때 암시적으로 주어지는 스코프 => 전역스코프
// 전역변수는 써야하지만, 남용하지는 말아야한다.

let name = "Irena"; // 전역
let age = 25; // 전역

function greet() {
    console.log(`Hello, ${name}!`);
}

function getBirthYear() {
    return new Date().getFullYear() - age;
}

console.log(greet());
console.log(getBirthYear());

// 이 방법의 문제는, 함수가 호출하는 컨텍스트(스코프)에 굉장히 의존적이라는점.

// 사용자 정보를 단일 객체에 보관하는 방법이 더 낫다.
let user = {
    name: "Irena",
    age: 25,
};

function greet2(user) {
    console.log(`Hello, ${user.name}!`);
}

function getBirthYear2(user) {
    return new Date().getFullYear() - user.age;
}
console.log(greet2(user));
console.log(getBirthYear2(user));