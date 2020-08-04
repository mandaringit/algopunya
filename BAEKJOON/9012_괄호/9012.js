const fs = require('fs');
const fileStream = fs.createReadStream('input.txt');
const readline = require('readline');

const rl = readline.createInterface({
  input: fileStream,
  output: process.stdout,
})
let i = 0
let N = null;
let brackets = [];

function isVPS(bracket) {
  const stack = [];
  for (let i = 0; i < bracket.length; i++) {
    const b = bracket[i]
    if (b === '(') {
      stack.push("(")
    } else {
      if (stack.length > 0 && stack[stack.length - 1] === '(') {
        stack.pop()
      } else {
        return "NO"
      }
    }
  }

  return stack.length === 0 ? 'YES' : 'NO'
}

rl.on("line", (line) => {
  if (i === 0) {
    N = Number(line);
    i++
  } else brackets.push(line)
})
  .on("close", () => {
    brackets.forEach(bracket => console.log(isVPS(bracket)))
    process.exit()
  })