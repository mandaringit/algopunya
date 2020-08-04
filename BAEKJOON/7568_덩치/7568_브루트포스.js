const readline = require('readline');
const fs = require('fs');
const fileStream = fs.createReadStream('input.txt');

const rl = readline.createInterface({
  input: fileStream,
  output: process.stdout,
})

let N = 0;
let input = [];
let i = 0

function solution(N, peoples) {
  const grades = Array(N).fill(1);
  for (let i = 0; i < N; i++) {
    for (let j = i + 1; j < N; j++) {
      const [A, B] = [peoples[i], peoples[j]];
      if (A[0] > B[0] && A[1] > B[1]) {
        grades[j]++;
      } else if (A[0] < B[0] && A[1] < B[1]) {
        grades[i]++;
      }
    }
  }

  return grades.join(" ");
}

rl.on('line', (line) => {
  if (i === 0) {
    N = Number(line);
    i++;
  } else {
    input.push(line.split(" ").map(Number))
  }

}).on('close', () => {
  console.log(solution(N, input))
  process.exit()
})