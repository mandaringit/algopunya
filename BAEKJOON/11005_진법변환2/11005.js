const fs = require('fs');
const fileStream = fs.createReadStream('input.txt');
const readline = require('readline');

const rl = readline.createInterface({
  input: fileStream,
  output: process.stdout,
})

let N = null; // 10진법 수
let B = null; // 진법

function conversion(resultArr, q) {
  if (B === 10) return q; // 10 진법 일땐 그냥 리턴

  const quotient = Math.floor(q / B); // 몫
  const remainder = q % B; // 나머지

  // 몫이 진법보다 작을때 -> 끝나는 경우
  if (quotient < B) {
    // 0일때 [0,0] 방지
    const newResult = quotient > 0 ? [quotient, remainder, ...resultArr] : [remainder, ...resultArr]
    return newResult
      .map(num => num + 55 >= 65 ? String.fromCharCode(num + 55) : num) // 10 이상은 문자로 변환
      .join('') // 모든 글자 합치기
  }

  // 아니라면 나머지 하나 품고 다시 진행
  resultArr = [remainder, ...resultArr];
  return conversion(resultArr, quotient);
}

rl.on("line", (line) => {
  [N, B] = line.split(" ").map(Number);
})
  .on("close", () => {
    console.log(conversion([], N))
    process.exit()
  })

