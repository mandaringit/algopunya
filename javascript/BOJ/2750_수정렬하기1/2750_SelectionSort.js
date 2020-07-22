const fs = require('fs');
const fileStream = fs.createReadStream('input.txt');
const readline = require('readline');

const rl = readline.createInterface({
  input: fileStream,
  output: process.stdout,
})

let N;
let input = []
let lineIdx = 0

function selectionSort(arr, N) {
  for (let i = N - 1; i > 0; i--) {
    let biggest = arr[i];
    let biggestIdx = i;
    for (let j = 0; j < i; j++) {
      const compare = arr[j]
      if (compare > biggest) {
        biggest = compare;
        biggestIdx = j;
      }
    }

    const temp = arr[i]
    arr[i] = arr[biggestIdx];
    arr[biggestIdx] = temp;
  }
  return arr;
}

rl.on("line", (line) => {
  if (lineIdx === 0) {
    N = Number(line)
    lineIdx++;
  } else {
    input.push(Number(line))
  }
})
  .on("close", () => {
    // 로직
    selectionSort(input, N).forEach(v => console.log(v));
    process.exit()
  })