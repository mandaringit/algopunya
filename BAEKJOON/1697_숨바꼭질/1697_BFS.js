const fs = require('fs');
const fileStream = fs.createReadStream('input.txt');
const readline = require('readline');

const rl = readline.createInterface({
  input: fileStream,
  output: process.stdout,
});

let input = [];

function solution(N, K) {
  if (N === K) return 0;

  const checked = Array(100001).fill(-1);

  let front = 0;
  let rear = 0;
  const q = [N];
  checked[N] = 0; // 시작점
  rear++;

  while (front !== rear) {
    const x = q[front];
    front++;

    for (let nx of [x + 1, x - 1, 2 * x]) {
      // 범위 안 & 방문 안함
      if (nx >= 0 && nx <= 100000 && checked[nx] === -1) {
        checked[nx] = checked[x] + 1; // 초 기록

        // 종료 조건
        if (nx === K) {
          return checked[nx];
        }

        q.push(nx);
        rear++;
      }
    }
  }
}

rl.on('line', (line) => {
  input.push(line);
  // 줄별로 해야할 작업
}).on('close', () => {
  const [N, K] = input[0].split(' ').map(Number);
  console.log(solution(N, K));
  process.exit();
});
