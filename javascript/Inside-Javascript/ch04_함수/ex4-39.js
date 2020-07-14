function Person(name, age, hobby) {
  this.name = name;
  this.age = age;
  this.hobby = hobby;
}

const foo = new Person('foo', 30, 'tennis');

console.log(foo.hasOwnProperty('name'));

console.dir(Person.prototype);