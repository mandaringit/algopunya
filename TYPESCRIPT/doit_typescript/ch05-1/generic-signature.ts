const normal = (cb: (number) => number): void => {};
const error = (cb: (number, number?) => number): void => {};
const fixed = (cb: (a: number, number?) => number): void => {};

const f = <T>(cb: (arg: T, i?: number) => number): void => {};
