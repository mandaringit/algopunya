const fs = require('fs');
const fileStream = fs.createReadStream('input.txt');
const readline = require('readline');

const rl = readline.createInterface({
  input: fileStream,
  output: process.stdout,
});

let words;

function solution(words) {
  const [A, B] = words.split(' ');
  let minCount = A.length;
  for (let i = 0; i <= B.length - A.length; i++) {
    const Bpart = B.slice(i, i + A.length);
    let count = 0;
    for (let j = 0; j < A.length; j++) {
      A[j] !== Bpart[j] && count++;
    }
    minCount = count < minCount ? count : minCount;
  }
  return minCount;
}

rl.on('line', (line) => {
  words = line;
}).on('close', () => {
  console.log(solution(words));
  process.exit();
});
