const fs = require('fs');
const fileStream = fs.createReadStream('input.txt');
const readline = require('readline');

const rl = readline.createInterface({
  input: fileStream,
  output: process.stdout,
});

let expression;

function solution(expression) {
  const numbers = expression.split('-');
  return numbers
    .map((plusExpression) =>
      plusExpression
        .split('+')
        .map(Number) // Number('') = 0으로 바뀜.
        .reduce((acc, curr) => acc + curr, 0)
    )
    .reduce((acc, curr, i) => (i === 0 ? acc + curr : acc - curr), 0);
}

rl.on('line', (line) => {
  expression = line;
}).on('close', () => {
  console.log(solution(expression));
  process.exit();
});
