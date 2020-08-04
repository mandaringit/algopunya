const fs = require('fs');
const fileStream = fs.createReadStream('input.txt');
const readline = require('readline');

const rl = readline.createInterface({
  input: fileStream,
  output: process.stdout,
});

let input = [];

function BFS(N, M, maze) {
  const checked = Array.from(Array(N), () => new Array(M).fill(0));
  const d = [
    [0, 1],
    [1, 0],
    [-1, 0],
    [0, -1],
  ];
  let front = 0;
  let rear = 0;
  const q = [[0, 0]];
  checked[0][0] = 1;
  rear++;

  while (front !== rear) {
    // dequeue
    const [i, j] = q[front];
    front++;

    for (let [dx, dy] of d) {
      const [ni, nj] = [i + dx, j + dy];
      // 범위 안
      if (ni >= 0 && ni < N && nj >= 0 && nj < M) {
        // 이동가능한 길 & 아직 안간곳
        if (maze[ni][nj] === 1 && checked[ni][nj] === 0) {
          checked[ni][nj] = checked[i][j] + 1; // 방문표시 & 거리
          if (ni === N - 1 && nj === M - 1) break; // 목적지면 그만
          // 아니면 다음으로
          // enqueue
          q.push([ni, nj]);
          rear++;
        }
      }
    }
  }

  return checked[N - 1][M - 1];
}

rl.on('line', (line) => {
  input.push(line);
}).on('close', () => {
  const [N, M] = input[0].split(' ').map(Number);
  const maze = input.slice(1).map((line) => line.split('').map(Number));
  console.log(BFS(N, M, maze));
  process.exit();
});
