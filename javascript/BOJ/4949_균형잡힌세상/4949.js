const fs = require('fs');
const fileStream = fs.createReadStream('input.txt');
const readline = require('readline');

const rl = readline.createInterface({
  input: fileStream,
  output: process.stdout,
})

let input = []

function isBeautifulWorld(sentence) {
  const stack = [];
  const pair = {
    "[": "]",
    "(": ")",
  }
  for (let i = 0; i < sentence.length; i++) {
    const char = sentence[i];
    if (char === '(' || char === '[') {
      stack.push(char)
    } else if (char === ')' || char === ']') {
      if (stack.length > 0 && pair[stack[stack.length - 1]] === char) {
        stack.pop()
      } else {
        return 'no'
      }
    }
  }
  return stack.length > 0 ? 'no' : 'yes';
}

rl.on("line", (line) => {
  input.push(line);
})
  .on("close", () => {
    input.slice(0,input.length-1).forEach(sentence => console.log(isBeautifulWorld(sentence)));
    process.exit()
  })