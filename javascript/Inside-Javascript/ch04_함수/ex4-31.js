function Person(name, age, gender) {
  this.name = name;
  this.age = age;
  this.gender = gender;
}

const foo = {};

Person.apply(foo, ['foo', 30, 'man'])
console.dir(foo)

Person.call(foo, 'foo', 30, 'main')
console.dir(foo)
