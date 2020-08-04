const fs = require('fs');
const fileStream = fs.createReadStream('input.txt');
const readline = require('readline');

const rl = readline.createInterface({
  input: fileStream,
  output: process.stdout,
})

let N = null;
let papers = []
let i = 0;

function cuttingPaper(N, papers) {
  const result = [0, 0]

  // 색 통일 확인용
  function isUnity(i1, i2, j1, j2) {
    const c = [0, 0];
    for (let k = i1; k < i2; k++) {
      for (let m = j1; m < j2; m++) {
        c[papers[k][m]]++;
        if (c[0] > 0 && c[1] > 0) return false;
      }
    }
    return true;
  }

  function cutting(row1, row2, col1, col2) {
    if (isUnity(row1, row2, col1, col2)) {
      const color = papers[row1][col1];
      result[color]++;
    } else {
      const diff = Math.abs(row2 - row1) / 2
      cutting(row1, row2 - diff, col1, col2 - diff)
      cutting(row1, row2 - diff, col2 - diff, col2)
      cutting(row2 - diff, row2, col1, col2 - diff)
      cutting(row2 - diff, row2, col2 - diff, col2)
    }
  }

  cutting(0, N, 0, N)
  return result
}

rl.on("line", (line) => {
  // 줄별로 해야할 작업
  if (i === 0) N = Number(line);
  else papers.push(line.split(" ").map(Number))
  i++;
})
  .on("close", () => {
    cuttingPaper(N, papers).forEach((v) => console.log(v))
    process.exit()
  })