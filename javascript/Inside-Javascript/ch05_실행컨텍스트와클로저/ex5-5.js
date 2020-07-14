const value = "value1";

function printFunc() {
  const value = "value2";

  function printValue() {
    return value;
  }

  console.log(printValue());
}

printFunc();