function callLater(obj, a, b) {
  return (function () {
    obj["sum"] = a + b;
    console.log(obj["sum"])
  });
}

const sumObj = {
  sum: 0,
}

const func = callLater(sumObj, 1, 2);
setTimeout(func, 500);