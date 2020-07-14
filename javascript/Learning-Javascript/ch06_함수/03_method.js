// 객체의 프로퍼티인 함수 -> 메서드

// ES5
const o = {
    name: "Wallace", // 원시 값 프로퍼티
    bark: function () { // 함수 프로퍼티 (메서드)
        return 'Woof!';
    }
};
console.log(o.bark());
const o2 = {
    name: 'Wallace',
    bark() {
        return 'Woof!'
    },
};
console.log(o2.bark());

