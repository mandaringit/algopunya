// 객체나 배열을 변수로 '해체' 가능하다.

const obj = {b: 2, c: 3, d: 4};

// 해체할당
const {a, b, c} = obj;
console.log(a, b, c);

// 객체를 해체할 때는 반드시 변수 이름과 객체의 프로퍼티 이름이 일치해야한다.
// 프로퍼티 이름이 유효한 식별자인 프로퍼티만 해체 후 할당된다.

const obj2 = {b1: 2, c1: 3, d1: 4};
let a1, b1, c1;
// {a,b,c} = obj;  // error => 좌변을 블록으로 인식한다.
({a1, b1, c1} = obj2);  // 괄호를 사용해야한다.
console.log(a1, b1, c1);


// 배열해체 (이터러블 객체도 해체 가능)
const arr = [1, 2, 3];
let [x, y] = arr; // 변수 이름은 마음대로 정할 수 있으며, 배열 순서대로 대응한다.
console.log(x, y);
// 확산 연산자 사용도 가능하다.
const arr2 = [1, 2, 3, 4, 5];
let [x1, x2, ...rest] = arr2;
console.log(x1, x2, rest);

// 변수의 값을 서로 바꾸는 것도 가능하다. (swap)
let k = 5, m = 10;
[k, m] = [m, k];
console.log(k, m);