function func() {
  let x = 1;
  return {
    func1: function () {
      console.log(++x);
    },
    func2: function () {
      console.log(-x);
    },
  };
}

const exam = func();
exam.func1();
exam.func2();