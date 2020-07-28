const readline = require('readline');
const fs = require('fs')
const fileStream = fs.createReadStream('input.txt');

const rl = readline.createInterface({
  input: fileStream,
  output: process.stdout,
})

const input = []

rl
  .on('line', (line) => {
    input.push(line)
  })
  .on('close', () => {
      const [N, M] = input[0].split(" ").map(Number);
      const numbers = input[1].split(" ").map(Number);
      let nearest = 0
      // 중복 없이 3개를 뽑아 합친다.
      for (let i = 0; i < N; i++) {
        for (let j = i + 1; j < N; j++) {
          for (let k = j + 1; k < N; k++) {
            const sum = numbers[i] + numbers[j] + numbers[k];
            if (sum <= M && sum > nearest) {
              nearest = sum
            }
          }
        }
      }
    console.log(nearest)
    process.exit()
    },
  );