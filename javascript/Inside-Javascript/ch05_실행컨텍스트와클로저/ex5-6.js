const value = "value1";

function printValue() {
  return value;
}

function printFunc(func) {
  const value = "value2";
  console.log(func());
}

printFunc(printValue)