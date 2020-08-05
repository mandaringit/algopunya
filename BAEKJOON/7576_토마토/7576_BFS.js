const fs = require('fs');
const fileStream = fs.createReadStream('input.txt');
const readline = require('readline');

const rl = readline.createInterface({
  input: fileStream,
  output: process.stdout,
});

let input = [];

// 익음 : 1, 익지 않음 : 0, 없음 : -1,
function solution(M, N, box) {
  const checked = Array.from(Array(N), () => new Array(M).fill(-1));
  let empty = 0;
  const d = [
    [0, 1],
    [1, 0],
    [-1, 0],
    [0, -1],
  ];
  const q = [];
  let front = 0;
  let rear = 0;
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
      if (box[i][j] === 1) {
        checked[i][j] = 0; // 익은 표시
        q.push([i, j]);
        rear++;
      } else if (box[i][j] === -1) {
        empty++;
      }
    }
  }

  while (front !== rear) {
    // dequeue
    const [i, j] = q[front];
    front++;
    for (let [dx, dy] of d) {
      const [ni, nj] = [i + dx, j + dy];
      // 범위 안
      if (ni >= 0 && ni < N && nj >= 0 && nj < M) {
        // 아직 안갔던 곳이고, 안익은 토마토라면
        if (checked[ni][nj] === -1 && box[ni][nj] === 0) {
          checked[ni][nj] = checked[i][j] + 1; // 인접 토마토 +1 일이 자신이 익는 날임.
          q.push([ni, nj]);
          rear++;
        }
      }
    }
  }

  // 전체 수 - 빈 공간이 토마토 수와 다르면 모두 못익힌 것.
  if (N * M - empty !== q.length) {
    return -1;
  }

  // q의 마지막 요소의 checked 값이 모두 익는 날이 된다.
  const [li, lj] = q[q.length - 1];
  return checked[li][lj];
}

rl.on('line', (line) => {
  input.push(line.split(' ').map(Number));
}).on('close', () => {
  const [M, N] = input[0];
  const tomatoBox = input.slice(1);
  const result = solution(M, N, tomatoBox);
  console.log(result);
  process.exit();
});
