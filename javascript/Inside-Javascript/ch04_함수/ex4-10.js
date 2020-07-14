const foo = function(func){
  func();
};

foo(function(){console.log('Function can be used as the argument.')});