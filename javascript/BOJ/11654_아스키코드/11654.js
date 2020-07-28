const fs = require('fs');
const fileStream = fs.createReadStream('input.txt');
const readline = require('readline');

const rl = readline.createInterface({
  input: fileStream,
  output: process.stdout,
})

let input = ''

rl.on("line", (line) => {
  // 줄별로 해야할 작업
  input = line;
})
  .on("close", () => {
    // 로직
    console.log(input.charCodeAt(0))
    process.exit()
  })