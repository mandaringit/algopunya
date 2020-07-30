const fs = require('fs');
const fileStream = fs.createReadStream('input.txt');
const readline = require('readline');

const rl = readline.createInterface({
  input: fileStream,
  output: process.stdout,
})

let N = null;
let given = null;
let M = null;
let search = null;
let i = 0;

function solution(N, M, given, search) {
  // 일단 정렬
  given.sort();

  function binarySearch(l, r, target) {
    while (l <= r) {
      const mid = Math.floor((l + r) / 2);
      const midValue = given[mid];
      if (midValue > target) r = mid - 1;
      else if (midValue < target) l = mid + 1;
      else return 1
    }
    return 0;
  }

  for (let num of search) {
    console.log(binarySearch(0, N - 1, num))
  }

}

rl.on("line", (line) => {
  if (i === 0) N = Number(line);
  else if (i === 1) given = line.split(" ").map(Number);
  else if (i === 2) M = Number(line);
  else search = line.split(" ").map(Number)
  i++
})
  .on("close", () => {
    solution(N, M, given, search)
    process.exit()
  })