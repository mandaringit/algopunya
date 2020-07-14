// 함수 표현식을 사용하면 즉시 호출하는 함수 표현식 IIFE를 만들 수 있다.
// IIFE는 함수를 선언하고 즉시 실행한다.
(function () {
    //IIFE 바디
})();

// 익명함수를 만들고, 그함수를 즉시 호출한다.
// 내부에 자신만의 스코프를 가지지만, 자체가 함수이므로 스코프 밖으로 무언가를 내보낼 수 있다.

const message = (function () {
    const secret = "I'm secret!"; // 외부에서 접근 불가하다.
    return `The Secret is ${secret.length} Characters long.`
})();
console.log(message);

const f = (() => {
    let count = 0;
    return () => `I have been called ${++count} time(s).`
})();
console.log(f());
console.log(f());