const fs = require('fs');
const fileStream = fs.createReadStream('input.txt');
const readline = require('readline');

const rl = readline.createInterface({
  input: fileStream,
  output: process.stdout,
});

let ln = 0;
let inputIdx = -1;
let T;
let inputs = [];

function solution(input) {
  const scores = input.slice(1).map((score) => score.split(' ').map(Number));
  const sortedByPaper = [...scores].sort((a, b) => a[0] - b[0]);
  const hired = [sortedByPaper[0]];

  for (let i = 1; i < sortedByPaper.length; i++) {
    const candidate = sortedByPaper[i];
    candidate[1] < hired[hired.length - 1][1] && hired.push(candidate);
  }

  return hired.length;
}

rl.on('line', (line) => {
  if (ln === 0) {
    T = Number(line);
    inputs = Array.from(Array(T), () => new Array(0));
    ln++;
  } else {
    if (line.split(' ').length === 1) {
      inputIdx++;
    }
    inputs[inputIdx].push(line);
  }
}).on('close', () => {
  for (let t = 0; t < T; t++) {
    console.log(solution(inputs[t]));
  }
  process.exit();
});
