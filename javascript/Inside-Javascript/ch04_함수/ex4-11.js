const foo = function(){
  return function () {
    console.log('this function is the return value')
  }
};

const bar = foo();
bar();