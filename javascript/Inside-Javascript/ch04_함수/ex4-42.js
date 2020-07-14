function Person(name) {
  this.name = name;
}

Person.prototype.getName = function () {
  return this.name;
}

const foo = new Person('foo');

console.log(foo.getName()); // foo 가 호출 했으니 foo.name

Person.prototype.name = 'person';

console.log(Person.prototype.getName()) // Person.prototype이 호출했으니 Person.prototype.name