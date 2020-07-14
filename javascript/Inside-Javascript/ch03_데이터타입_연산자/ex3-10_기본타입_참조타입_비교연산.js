const a = 100;
const b = 100;

const objA = {value: 100};
const objB = {value: 100};
const objC = objB;

console.log(a == b);
console.log(objA == objB);
console.log(objB == objC);