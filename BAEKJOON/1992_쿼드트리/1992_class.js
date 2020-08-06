const fs = require('fs');
const fileStream = fs.createReadStream('input.txt');
const readline = require('readline');

const rl = readline.createInterface({
  input: fileStream,
  output: process.stdout,
});

let input = [];

class QuadTree {
  constructor(N, video) {
    this.video = video;
    this.N = N;
  }

  // 압축하는 함수
  zip(range, i, j) {
    if (range === this.N) return this.zippedDigit(range, i, j);
    // 왼쪽 위 , 오른쪽 위, 왼쪽 아래, 오른쪽 아래 모서리
    const points = [
      [i, j],
      [i, j + range],
      [i + range, j],
      [i + range, j + range],
    ];
    const [lt, rt, lb, rb] = points.map(([pi, pj]) =>
      this.zippedDigit(range, pi, pj)
    );

    return `(${lt}${rt}${lb}${rb})`;
  }

  // 해당 범위가 압축 가능한가?
  zippedDigit(range, i, j) {
    const colors = [0, 0]; // 0은 흰색 1은 검정
    for (let k = 0; k < range; k++) {
      for (let m = 0; m < range; m++) {
        const [ni, nj] = [i + k, j + m];
        const color = this.video[ni][nj];
        colors[color]++;
      }
    }
    // 섞인 경우 해당 범위 다시 묶는 작업 수행
    if (colors[0] && colors[1]) return this.zip(range / 2, i, j);
    // 아니라면 압축한 문자열 리턴
    else {
      if (colors[0] === range * range) {
        return '0';
      } else {
        return '1';
      }
    }
  }
}

rl.on('line', (line) => {
  input.push(line);
  // 줄별로 해야할 작업
}).on('close', () => {
  const N = Number(input[0]);
  const video = input.slice(1).map((line) => line.split('').map(Number));
  const qt = new QuadTree(N, video);
  console.log(qt.zip(N, 0, 0));
  process.exit();
});
