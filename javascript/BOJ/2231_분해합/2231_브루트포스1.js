const readline = require('readline');
const fs = require('fs');
const fileStream = fs.createReadStream('input.txt')

const rl = readline.createInterface({
  input: fileStream,
  output: process.stdout,
})

let input = '';

function getDecompositionSum(n) {
  const digitSum = n.toString().split("").map(Number).reduce((acc, curr) => acc + curr, 0);
  return Number(n) + digitSum
}

rl.on('line', (line) => {
  input = line
})
  .on('close', () => {
    const target = Number(input)
    let i = 0;
    let smallDeNum = 0;
    while(i < target){
      if(getDecompositionSum(i) === target){
        smallDeNum = i;
        break
      }
      i++
    }
    console.log(smallDeNum)
    process.exit();
  })