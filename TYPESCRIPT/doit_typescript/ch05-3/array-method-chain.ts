const multiply = (result, val) => result * val;

const numbers: number[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

const tempResult = numbers
  .filter((num) => num % 2 !== 0)
  .map((num) => num * num)
  .reduce(multiply, 1);

const result = Math.round(Math.sqrt(tempResult));
console.log(result);
