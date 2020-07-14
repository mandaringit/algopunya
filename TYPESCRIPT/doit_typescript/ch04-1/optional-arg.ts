function fn(arg1: string, arg?: number) {
  console.log(`arg:${arg}`);
}

fn('hello', 1);
fn('hello');

type optionalArgFunc = (string, number?) => void;
const fn2: optionalArgFunc = (arg1: string, arg?: number): void => {};
