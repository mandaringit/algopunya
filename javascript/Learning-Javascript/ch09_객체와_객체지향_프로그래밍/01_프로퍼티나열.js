// 프로퍼티는 "키"(문자열 또는 심볼)와 "값"으록 구성된다.
// 객체의 진짜 특징은, 키를 통해 프로퍼티에 접근할 수 있다는 점이다.

// ***객체의 프로퍼티에는 순서가없다!!

const SYM = Symbol();
const obj = {a: 1, b: 2, c: 3, [SYM]: 4};


// for .. in ..
for (let prop in obj) {
    if (!obj.hasOwnProperty(prop)) continue;
    console.log(`${prop}: ${obj[prop]}`) // 키가 심볼인 프로퍼티는 미포함.
}

// Object.keys()
// 객체에서 나열 가능한 문자열 프로퍼티를 "배열"로 반환.
// hasOwnProperty 를 확인할 필요가 없어 객체의 프로퍼티 키를 배열로 가져올때는 이게 낫다.
console.log(Object.keys(obj));
Object.keys(obj).forEach(prop => console.log(`${prop} : ${obj[prop]}`));

// 객체에서 'x'로 시작하는 프로퍼티 가져오기.
const o = {apple: 1, xochitl: 2, balloon: 3, guitar: 4, xylophone: 5};
Object.keys(o)
    .filter(prop => prop.match(/^x/))
    .forEach(prop => console.log(`${prop}: ${o[prop]}`));

