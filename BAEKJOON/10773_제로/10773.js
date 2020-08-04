const fs = require('fs');
const fileStream = fs.createReadStream('input.txt');
const readline = require('readline');

const rl = readline.createInterface({
  input: fileStream,
  output: process.stdout,
})
let i = 0
let N = null
let input = []

function solution(numbers){
  const account = [];
  numbers.forEach(num => num === '0' ? account.pop() : account.push(Number(num)))
  return account.reduce((acc,curr) => acc + curr,0)
}

rl.on("line", (line) => {
  if (i === 0) {
    N = Number(line)
    i++
  } else {
    input.push(line)
  }
})
  .on("close", () => {
    console.log(solution(input))
    process.exit()
  })