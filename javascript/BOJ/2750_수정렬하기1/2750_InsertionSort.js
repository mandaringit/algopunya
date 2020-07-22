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

function InsertionSort(arr, N) {
  // 1번째 인덱스부터 시작하여
  for (let i = 1; i < N; i++) {
    let idx = i;
    // 비교대상 < 비교대상 이전 && 비교대상 인덱스가 0보다 크거나 같다면
    while (arr[idx] < arr[idx - 1] && idx >= 0) {
      // 비교대상과 비교대상 이전을 스왑
      const temp = arr[idx];
      arr[idx] = arr[idx - 1];
      arr[idx - 1] = temp;
      // 다음 비교를 위해 idx 감소
      idx--;
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
    InsertionSort(input, N).forEach(v => console.log(v));
    process.exit()
  })