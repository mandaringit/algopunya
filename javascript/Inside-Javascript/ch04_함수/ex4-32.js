function myFunction() {
  console.dir(arguments)
  // arguments.shift(); // 에러

  const args = Array.prototype.slice.apply(arguments);
  console.dir(args)
}

myFunction(1, 2, 3)
