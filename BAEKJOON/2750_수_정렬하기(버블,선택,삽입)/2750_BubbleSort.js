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

function bubbleSort(arr, N) {
  // 마지막이 정렬되는건 선택 정렬이랑 똑같다.
  for (let i = N - 1; i > 0; i--) {
    // 처음부터 i까지 서로 비교해가면서 바꿔간다.
    for (let j = 0; j < i; j++) {
      // swap
      let temp = arr[j];
      if (arr[j] > arr[j + 1]) {
        arr[j] = arr[j + 1];
        arr[j + 1] = temp;
      }
    }
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
    bubbleSort(input, N).forEach(v => console.log(v));
    process.exit()
  })