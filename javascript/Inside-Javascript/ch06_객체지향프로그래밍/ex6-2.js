function Person(arg) {
  this.name = arg;
}

Person.prototype.getName = function () {
  return this.name;
}

Person.prototype.setName = function (value) {
  this.name = value;
}

const me = new Person("me");
const you = new Person("you");
console.log(me.getName());
console.log(you.getName());