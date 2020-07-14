const foo = {
  name: 'foo',
  age: 35,
  gender: 'man',
}

console.dir(foo);

function Person(name, age, gender, position) {
  this.name = name;
  this.age = age;
  this.gender = gender;
}

const bar = new Person('bar', 33, 'woman');
console.dir(bar);

const baz = new Person('baz', 25, 'woman');
console.dir(baz)