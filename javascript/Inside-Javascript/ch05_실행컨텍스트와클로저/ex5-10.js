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

function saySomething(obj, methodName, name) {
  return (function (greeting) {
    return obj[methodName](greeting, name);
  });
}

function newObj(obj, name) {
  obj.func = saySomething(this, "who", name);
  return obj;
}

newObj.prototype.who = function (greeting, name) {
  console.log(greeting + " " + (name || "everyone"));
}

const obj1 = new newObj(objHello, "zzoonn");
obj1.call()