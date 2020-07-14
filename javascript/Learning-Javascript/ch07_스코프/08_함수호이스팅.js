// var 와 마찬가지로, 함수 선언도 스코프 맨 위로 끌어올려진다.
// 함수 선언 전 호출이 가능하다.

f();
function f() {
    return console.log('f');
}

// 다만, 변수에 할당한 함수 표현식은 끌어올려지지 않는다.
// 이들은 변수의 규칙을 따르기 때문.

x(); // 에러
const x = function(){
    return console.log('x');
};



