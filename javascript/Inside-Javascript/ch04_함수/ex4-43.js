function Person(name) {
  this.name = name;
}

console.log(Person.prototype.constructor);

const foo = new Person('foo');
console.log(foo.country)

Person.prototype = {
  conutry: 'korea',
}
console.log(Person.prototype.constructor);

const bar = new Person('bar');
console.log(foo.conutry);
console.log(bar.conutry);
console.log(foo.constructor);
console.log(bar.constructor);