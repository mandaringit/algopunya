const fs = require("fs");
const fileStream = fs.createReadStream("input.txt");
const readline = require("readline");

const rl = readline.createInterface({
  input: fileStream,
  output: process.stdout,
});

let input = [];

function solution(N, M, givenNumbers, searchNumbers) {
  const sortedGivenNumbers = [...givenNumbers].sort((a, b) => a - b);
  searchNumbers.forEach((num) =>
    console.log(binarySearch(sortedGivenNumbers, num) ? 1 : 0)
  );
}

function binarySearch(arr, number) {
  let left = 0;
  let right = arr.length - 1;
  while (left <= right) {
    const mid = Math.floor((left + right) / 2);
    const midValue = arr[mid];
    if (midValue < number) {
      left = mid + 1;
    } else if (midValue > number) {
      right = mid - 1;
    } else {
      return true;
    }
  }
  return false;
}

rl.on("line", (line) => {
  input.push(line);
}).on("close", () => {
  // 로직
  const N = Number(input[0]);
  const M = Number(input[2]);
  const givenNumbers = input[1].split(" ").map(Number);
  const searchNumbers = input[3].split(" ").map(Number);
  solution(N, M, givenNumbers, searchNumbers);
  process.exit();
});
