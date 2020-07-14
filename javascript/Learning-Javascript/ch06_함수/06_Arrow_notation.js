// 간단히 말하면, function 이라는 단어와,
// 중괄호 숫자를 줄이려고 고안된 단축문법

// 화살표 함수는 항상 익명이다.
// 변수에 할당은 가능하지만, function 키워드 처럼 이름 붙은 함수를 만들 순 없다.

// 1. function 생략 가능
const f1 = function () {
    return "hello!"
};
const f1_2 = () => "hello";

// 2. 함수에 매개변수가 단 하나 뿐이라면 괄호(()) 도 생략 가능.
const f2 = function (name) {
    return `Hello,${name}!`
};
const f2_2 = name => `hello, ${name}`;

// 3. 함수 바디가 표현식 하나라면 중괄호와 return 문도 생략 가능
const f3 = function (a, b) {
    return a + b;
};
const f3_2 = (a, b) => a + b;

// 화살표 함수와 일반적인 함수의 차이점 1 => this가 다른 변수와 마찬가지로, 정적(lexically)으로 묶인다는 것.
// 이전 예제에서 화살표 함수를 쓰면 this가 사용 가능하다.
const o2 = {
    name: 'Julie',
    greetBackwards: function () {
        const getReverseName = () => {
            let nameBackwards = '';
            for (let i = this.name.length - 1; i >= 0; i--) {
                nameBackwards += this.name[i];
            }
            return nameBackwards;
        };
        return `${getReverseName()} si eman ym ,olleH`;
    },
};
console.log(o2.greetBackwards());

// 차이점2 => 객체 생성자로 사용할 수 없다
// 차이점3 => arguments 변수도 사용할 수 없다. (확산연산자를 쓰면 된다.)
