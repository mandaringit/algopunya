const fs = require('fs');
const fileStream = fs.createReadStream('input.txt');
const readline = require('readline');

const rl = readline.createInterface({
  input: fileStream,
  output: process.stdout,
})

let ln = 0;
let N = null;
let map = []

function DFS(i, j, number, checked) {
  const stack = [[i, j]];
  checked[i][j] = number; // 방문 표시

  while (stack.length > 0) {
    const [i_, j_] = stack.pop();
    const d = [[0, 1], [1, 0], [0, -1], [-1, 0]];

    for (let [dx, dy] of d) {
      const ni = i_ + dx;
      const nj = j_ + dy;

      if (ni >= 0 && ni < N && nj >= 0 && nj < N) {
        if (checked[ni][nj] === 0 && map[ni][nj] > 0) {
          checked[ni][nj] = number;
          stack.push([ni, nj])
        }
      }
    }
  }

}

function solution(map) {
  const checked = Array.from(Array(N), () => new Array(N).fill(0))
  let mapNumber = 0;

  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      if (map[i][j] === '1' && checked[i][j] === 0) {
        mapNumber++;
        DFS(i, j, mapNumber, checked)
      }
    }
  }

  let counter = Array(mapNumber + 1).fill(0);
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      counter[checked[i][j]]++;
    }
  }
  counter = counter.slice(1).sort((a, b) => a > b ? 1 : -1)
  return [mapNumber, ...counter]
}

rl.on("line", (line) => {
  if (ln === 0) N = Number(line);
  else map.push(line);
  ln++
})
  .on("close", () => {
    solution(map).forEach(v => console.log(v))
    process.exit()
  })