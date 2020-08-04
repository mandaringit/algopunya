const readline = require('readline');
const fs = require('fs');
const fileStream = fs.createReadStream('input.txt')

const rl = readline.createInterface({
  input: fileStream,
  output: process.stdout,
})

let input = '';

function solution(target) {
  for (let i = 0; i < target; i++) {
    let part = i;
    let sum = i;
    while (part > 0) {
      sum += part % 10;
      part = Math.floor(part / 10);
    }
    if (sum === target) return i
  }
  return 0
}

rl.on('line', (line) => {
  input = line;
})
  .on('close', () => {
    console.log(solution(Number(input)))
    process.exit();
  })