// 함수가 특정 스코프에 접근할 수 있도록 의도적으로 그 스코프에서 정의하는 경우가 많다.
// 클로저라고 한다.
// 스코프를 함수 주변으로 좁히는 것이라고 생각해도 된다.

let globalFunc;
{
    let blockVar = 'a';
    globalFunc = function () {
        console.log(blockVar);
    }
}
console.log(typeof blockVar); // 원래 바깥에선 접근하지 못하지만,
globalFunc(); // 안에서 정의된 함수는 해당 스코프에 접근 가능하다.

//일반적으로 접근할 수 없는 것에 접근 할 수있는 효과도 있다.
let f;
{
    let o = {note: 'Safe'};
    f = () => o;
}
let oRef = f(); // 기존 스코프에서는 o에 접근 불가하지만, f()를 통해 접근이 가능해진다.
oRef.note = "Not so safe after all!";
console.log(oRef);
