function myFunction(){
  return true;
}

console.dir(myFunction.prototype);
console.dir(myFunction.prototype.constructor);

(function (name) {
  console.log('THIS iS the immediate function -->' + name)
})('foo');

function parent(){
  const a = 100;
  const b = 200;

  function child(){
    const b = 300;
    console.log(a);
    console.log(b);
  }
  child()
}

parent();
child();