function HelloFunc(func) {
  this.greeting = "hello";
}

HelloFunc.prototype.call = function (func) {
  func ? func(this.greeting) : this.func(this.greeting);
}

const userFunc = function (greeting) {
  console.log(greeting);
}

const objHello = new HelloFunc();
objHello.func = userFunc;
objHello.call();