function Person(name) {
  this.name = name;
}

Person.prototype.country = 'Korea';

const foo = new Person('foo');
const bar = new Person('bar');
console.log(foo.country);
console.log(bar.country);
foo.country = 'USA';

console.log(foo.country);
console.log(bar.country);