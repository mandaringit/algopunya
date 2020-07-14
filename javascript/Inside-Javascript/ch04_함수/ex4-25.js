const test = 'This is test';

const sayFoo = function () {
  console.log(this.test)
}

sayFoo()