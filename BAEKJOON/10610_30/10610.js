const fs = require('fs');
const fileStream = fs.createReadStream('input.txt');
const readline = require('readline');

const rl = readline.createInterface({
  input: fileStream,
  output: process.stdout,
});

let input;

function solution(number) {
  const numberArr = number
    .split('')
    .map(Number)
    .sort((a, b) => b - a);
  if (
    numberArr[numberArr.length - 1] === 0 &&
    numberArr.reduce((acc, curr) => acc + curr, 0) % 3 === 0
  ) {
    return numberArr.join('');
  }
  return -1;
}

rl.on('line', (line) => {
  input = line;
}).on('close', () => {
  console.log(solution(input));
  process.exit();
});
