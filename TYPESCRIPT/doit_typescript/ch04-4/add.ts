export type NumberToNumberFunc = (number) => number;

export const add = (a: number): NumberToNumberFunc => {
  const _add: NumberToNumberFunc = (b: number) => {
    return a + b;
  };

  return _add;
};
