function outerFunc(arg1, arg2) {
  const local = 8;

  function innerFunc(innerArg) {
    console.log((arg1 + arg2) / (innerArg + local))
  }

  return innerFunc
}

const exam1 = outerFunc(2, 4);
exam1(2);