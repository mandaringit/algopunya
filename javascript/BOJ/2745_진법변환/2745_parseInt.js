const fs = require('fs');
const fileStream = fs.createReadStream('input.txt');
const readline = require('readline');

const rl = readline.createInterface({
  input: fileStream,
  output: process.stdout,
})

let N = null; // B진법 수 N
let B = null; // B진법

rl.on("line", (line) => {
  [N, B] = line.split(" ");
  B = Number(B);
})
  .on("close", () => {
    console.log(parseInt(N, B));
    process.exit()
  })
