// 함수 표현식
const f = function () {
    return 'function expression'
};

console.log(f());

// 함수에 이름을 정하고 다시 변수에 할당하는 경우
const g = function f(stop) {  // 재귀에 사용 가능하다.
    if (stop) console.log('f stopped');
    f(true);
};
g(false);

// 함수 선언과 함수 표현식을 구분 하는것은 '컨텍스트'이다.