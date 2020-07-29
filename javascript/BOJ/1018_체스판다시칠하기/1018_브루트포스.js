const readline = require('readline');
const fs = require('fs')
const fileStream = fs.createReadStream('input.txt');

const rl = readline.createInterface({
  input: fileStream,
  output: process.stdout,
})

let i = 0;
let N = 8;
let M = 8;
let board = [];

function solution(N, M, board) {
  let minValue = 64;
  for (let i = 0; i <= N - 8; i++) {
    for (let j = 0; j <= M - 8; j++) {
      let v1Count = 0;
      let v2Count = 0;
      for (let k = i; k < i + 8; k++) {
        for (let m = j; m < j + 8; m++) {
          // WBWBWBWB - BWBWBWBW 식
          const value = board[k][m];
          if (m % 2 === 0) {
            if (k % 2 === 0) {
              if (value === 'B') v1Count++;
              else v2Count ++
            } else {
              if (value === 'W') v1Count++;
              else v2Count++
            }
          } else {
            if (k % 2 === 0) {
              if (value === 'B') v2Count++;
              else v1Count ++
            } else {
              if (value === 'W') v2Count++;
              else v1Count++
            }
          }
        }
      }
      const small = Math.min(v1Count,v2Count)
      minValue = small < minValue ? small : minValue;
    }
  }
  return minValue
}

rl.on('line', (line) => {
  if (i === 0) {
    [N, M] = line.split(" ").map(Number);
    i++
  } else {
    board.push(line)
  }
}).on('close', () => {
  console.log(solution(N, M, board))
  process.exit()
})