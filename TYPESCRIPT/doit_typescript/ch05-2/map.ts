import { range } from './range';
import { fold } from './fold';

export const map = <T, Q>(
  array: T[],
  callback: (value: T, index?: number) => Q
): Q[] => {
  let result: Q[] = [];
  for (let index = 0; index < array.length; ++index) {
    const value = array[index];
    result = [...result, callback(value, index)];
  }
  return result;
};

let numbers: number[] = range(1, 100 + 1);
let result = fold(
  map(numbers, (value) => value * value),
  (result, value) => result + value,
  0
);

console.log(result);
