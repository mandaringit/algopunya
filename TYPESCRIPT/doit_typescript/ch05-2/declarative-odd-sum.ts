import { range } from './range';
import { filter } from './filter';
import { fold } from './fold';

let numbers: number[] = range(1, 100 + 1);
const isOdd = (n: number): boolean => n % 2 !== 0;

let result = fold(filter(numbers, isOdd), (result, value) => result + value, 0);
console.log(result);
