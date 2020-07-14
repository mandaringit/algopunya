String.prototype.testMethod = function() {
  console.log("This is the String.prototype.testMethod()");
}

const str = "this is test";
str.testMethod();

console.dir(String.prototype)