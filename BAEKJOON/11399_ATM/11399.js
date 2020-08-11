const fs = require('fs');
const fileStream = fs.createReadStream('input.txt');
const readline = require('readline');

const rl = readline.createInterface({
  input: fileStream,
  output: process.stdout,
});

let input = [];

function solution(N, P) {
  const sortedP = [...P].sort((a, b) => (a > b ? 1 : -1));
  return sortedP
    .map((t, i) => sortedP.slice(0, i + 1).reduce((acc, curr) => acc + curr, 0))
    .reduce((acc, curr) => acc + curr, 0);
}

rl.on('line', (line) => {
  input.push(line);
}).on('close', () => {
  const N = Number(input[0]);
  const P = input[1].split(' ').map(Number);
  console.log(solution(N, P));
  process.exit();
});
