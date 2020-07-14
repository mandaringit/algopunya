// 이름과 함수를 받아 프로토타입의 속성으로 넣어버리는 method를 함수의 프로토타입에 넣어버림
Function.prototype.method = function (name, func) {
  this.prototype[name] = func;
}

function Person(arg) {
  this.name = arg;
}

Person.method("setName", function (value) {
  this.name = value;
});

Person.method("getName", function () {
  return this.name;
});

const me = new Person("me");
const you = new Person("you");
console.log(me.getName());
console.log(you.getName());
