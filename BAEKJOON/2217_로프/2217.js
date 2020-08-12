const fs = require('fs');
const fileStream = fs.createReadStream('input.txt');
const readline = require('readline');

const rl = readline.createInterface({
  input: fileStream,
  output: process.stdout,
});

let input = [];

function solution(N, ropes) {
  const sortedRopes = [...ropes].sort((a, b) => b - a);
  let maxWeight = 1;
  for (let k = 1; k <= N; k++) {
    // i 개 선택할 때 최대 중량은
    // 내림차순으로 정렬된 로프의 맨 앞에서 i - 1번째가 나눠받는 중량이다.
    const rope = sortedRopes[k - 1];
    // 걸리는 중량 w / i = rope, rope * i = w
    const w = rope * k;
    maxWeight = w > maxWeight ? w : maxWeight;
  }
  return maxWeight;
}

rl.on('line', (line) => {
  input.push(parseInt(line));
}).on('close', () => {
  const N = input[0];
  const ropes = input.slice(1);
  console.log(solution(N, ropes));
  process.exit();
});
