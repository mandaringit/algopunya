function Person(name) {
  this.name = name;
}

const foo = new Person('foo');

foo.sayHello() // 여기선 못씀

Person.prototype.sayHello = function () {
  console.log('Hello');
}

foo.sayHello();