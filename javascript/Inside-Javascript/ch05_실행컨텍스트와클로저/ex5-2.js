function execute(param1, param2) {
  const a = 1, b = 2;

  function func() {
    return a + b;
  }

  return param1 + param2 + func();
}

execute(3, 4);