function outerFunc(argNum) {
  let num = argNum; // 자유변수 값이 계속 변하니 주의.
  return function (x) {
    num += x;
    console.log('num: ' + num);
  }
}

const exam = outerFunc(40);
exam(5);
exam(-10);