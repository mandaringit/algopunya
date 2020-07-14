function getgreeting() {
    return "Hello world!";
}

// 명시적으로 리턴하지 않으면 undefined 리턴.
function getgreetingNotReturn() {
}

console.log(getgreeting());
console.log(getgreetingNotReturn());

// 넘기거나 할당 가능하다.
console.log(getgreeting()); // 호출 -> 실행
console.log(getgreeting); // 참초 -> 실행 X

const f = getgreeting; // 함수를 변수에 할당해 다른 이름으로 호출도 가능하다.
console.log(f());

const o = {};
o.f = getgreeting; // 객체 프로퍼티에 할당 가능.
console.log(o.f());

const arr = [1,2,3];
arr[1] = getgreeting; // 배열 요소로 할당 가능
arr[1]();


