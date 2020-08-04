const fs = require('fs');
const fileStream = fs.createReadStream('input.txt');
const readline = require('readline');

const rl = readline.createInterface({
  input: fileStream,
  output: process.stdout,
})

let N = null; // 10진법 수
let B = null; // 진법

rl.on("line", (line) => {
  [N, B] = line.split(" ").map(Number);
})
  .on("close", () => {
    console.log(N.toString(B).toUpperCase())
    process.exit()
  })

