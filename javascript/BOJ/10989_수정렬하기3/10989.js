const fs = require('fs')
const readline = require('readline')
const fileStream = fs.createReadStream('input.txt');

const rl = readline.createInterface({
  input: fileStream,
  output: process.stdout,
})

let input = []

function countingSort(N, arr) {
  const counting = Array(10000).fill(0);
  let maxValue = 1
  arr.forEach(v => {
    counting[v]++
    maxValue = v > maxValue ? v : maxValue;
  })
  let sorted = []
  for (let i = 1; i <= maxValue; i++) {
    const value = counting[i]
    sorted = [...sorted,...Array(value).fill(i)]
  }
  return sorted
}

rl.on('line', (line) => {
  input.push(line);
}).on('close', () => {
  N = Number(input[0]);
  countingSort(N, input.slice(1)).forEach(v => console.log(v))
  process.exit()
})