const fs = require('fs');
const fileStream = fs.createReadStream('input.txt');
const readline = require('readline');

const rl = readline.createInterface({
  input: fileStream,
  output: process.stdout,
})

let ln = 0;
let T = null;
let inputIdx = -1;
const inputs = [];

function DFS(i, j, field, checked, wormCnt, N, M) {
  const d = [[0, 1], [0, -1], [1, 0], [-1, 0]];
  const stack = [[i, j]];
  checked[i][j] = wormCnt;
  while (stack.length > 0) {
    const [i_, j_] = stack.pop();
    for (let [dx, dy] of d) {
      const [ni, nj] = [i_ + dx, j_ + dy];
      if (ni >= 0 && ni < N && nj >= 0 && nj < M) {
        if (checked[ni][nj] === 0 && field[ni][nj] === 1) {
          checked[ni][nj] = wormCnt;
          stack.push([ni, nj]);
        }
      }
    }
  }
}

function solution(t) {
  const input = inputs[t];
  const [M, N, K] = input[0];
  const field = Array.from(Array(N), () => new Array(M).fill(0));
  const checked = Array.from(Array(N), () => new Array(M).fill(0));
  for (let [X, Y] of input.slice(1)) {
    field[Y][X] = 1;
  }
  let wormCnt = 0
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
      if (field[i][j] === 1 && checked[i][j] === 0) {
        wormCnt++
        DFS(i, j, field, checked, wormCnt, N, M)
      }
    }
  }
  return wormCnt;
}

rl.on("line", (line) => {
  if (ln === 0) T = Number(line);
  else {
    const input = line.split(" ").map(Number);
    if (input.length === 3) {
      inputs.push([input]);
      inputIdx++;
    } else {
      inputs[inputIdx].push(input)
    }
  }
  ln++
})
  .on("close", () => {
    for (let t = 0; t < T; t++) {
      console.log(solution(t))
    }
    process.exit()
  })