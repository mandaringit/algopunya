function Person(name) {
  this.name = name;
}

const foo = new Person('foo');
console.dir(Person);
console.dir(foo);

function a() {
  console.log("hi")
}

console.dir(a)