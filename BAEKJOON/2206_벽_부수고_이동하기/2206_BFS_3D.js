const fs = require('fs');
const fileStream = fs.createReadStream('input.txt');
const readline = require('readline');

const rl = readline.createInterface({
  input: fileStream,
  output: process.stdout,
});

let input = [];

function solution(N, M, maze) {
  // 3d arr

  const checked = Array.from(Array(N), () =>
    Array.from(Array(M), () => new Array(2).fill(0))
  );
  const d = [
    [0, 1],
    [0, -1],
    [1, 0],
    [-1, 0],
  ];
  let front = 0;
  let rear = 0;
  const q = [[0, 0, 0]]; // i, j, crash
  rear++;
  checked[0][0][0] = 1;

  while (front !== rear) {
    // dequeue
    const [i, j, crash] = q[front];
    front++;

    // 탈출 조건
    if (i === N - 1 && j === M - 1) return checked[i][j][crash];

    for (let [dx, dy] of d) {
      const [ni, nj] = [i + dx, j + dy];

      // 범위 안
      if (ni >= 0 && ni < N && nj >= 0 && nj < M) {
        // 미방문
        if (checked[ni][nj][crash] === 0) {
          // 갈수 있는 길
          if (maze[ni][nj] === 0) {
            checked[ni][nj][crash] = checked[i][j][crash] + 1;
            rear++;
            q.push([ni, nj, crash]);
            // console.log(checked) // 가는 모습을 봐도 이해하는데 도움.
          } else if (maze[ni][nj] === 1 && crash === 0) {
            // 길이 없지만 부술수 있는 곳
            checked[ni][nj][1] = checked[i][j][crash] + 1;
            rear++;
            q.push([ni, nj, 1]);
            // console.log(checked) // 가는 모습을 봐도 이해하는데 도움.
          }
        }
      }
    }
  }
  // 탈출 못하면
  return -1;
}

rl.on('line', (line) => {
  input.push(line);
}).on('close', () => {
  // 로직
  const [N, M] = input[0].split(' ').map(Number);
  const maze = input.slice(1).map((line) => line.split('').map(Number));
  const result = solution(N, M, maze);
  console.log(result);
  process.exit();
});
