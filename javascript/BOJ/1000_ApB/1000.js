const fs = require('fs');
const fileStream = fs.createReadStream('input.txt');
const readline = require('readline');

const rl = readline.createInterface({
  input: fileStream,
  output: process.stdout,
})
let input = []
rl.on("line", (line) => input = line.split(" ").map(Number))
  .on("close", () => {
    const [a, b] = input;
    console.log(a + b);
    process.exit()
  })
