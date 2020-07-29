const fs = require('fs');
const fileStream = fs.createReadStream('input.txt');
const readline = require('readline');

const rl = readline.createInterface({
  input: fileStream,
  output: process.stdout,
})

let N = null

function solution(N) {
  let cards = [];
  let front = 0;
  let rear = N;
  for (let i = 1; i <=N; i++) {
    cards.push(i);
  }
  // 두개를 dequeue()하고, 맨 앞으로 하나를 붙임
  while (front+1 !== rear) {
    front += 1
    const x = cards[front];
    cards.push(x);
    rear += 1
    front += 1
  }
  return cards[front]
}

rl.on("line", (line) => {
  N = Number(line);
})
  .on("close", () => {
    console.log(solution(N))
    process.exit()
  })