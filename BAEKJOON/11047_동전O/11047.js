const fs = require('fs');
const fileStream = fs.createReadStream('input.txt');
const readline = require('readline');

const rl = readline.createInterface({
  input: fileStream,
  output: process.stdout,
});

let input = [];

function solution(N, K, coins) {
  let coinCount = 0;
  // 큰수부터.
  for (let i = coins.length - 1; i >= 0; i--) {
    const price = coins[i];
    const quotient = Math.floor(K / price);
    const remainder = K % price;
    // 몫이 있으면
    if (quotient > 0) {
      coinCount += quotient;
      K = remainder;
    }
  }

  return coinCount;
}

rl.on('line', (line) => {
  input.push(line);
}).on('close', () => {
  const [N, K] = input[0].split(' ').map(Number);
  const coins = input.slice(1).map(Number);
  console.log(solution(N, K, coins));
  process.exit();
});
