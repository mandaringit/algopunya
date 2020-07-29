const fs = require('fs');
const fileStream = fs.createReadStream('input.txt');
const readline = require('readline');

const rl = readline.createInterface({
  input: fileStream,
  output: process.stdout,
})

let input = []

class Stack {
  constructor(N) {
    this.stack = Array(N).fill(0);
    this.top = -1;
  }

  push(num) {
    this.top += 1
    this.stack[this.top] = num;
  }

  pop() {
    if (this.top > -1) {
      const value = this.stack[this.top];
      this.stack[this.top] = 0;
      this.top -= 1;
      return value;
    } else {
      return -1
    }
  }

  size() {
    return this.top + 1
  }

  empty() {
    return this.top > -1 ? 0 : 1;
  }

  getTop() {
    if (this.top > -1) {
      return this.stack[this.top]
    }
    return -1
  }
}

function stackProcess(N, cmds) {
  const stack = new Stack(N)
  cmds.forEach(cmd => {
    cmd = cmd.split(" ");
    if (cmd[0] === 'push') {
      stack.push(Number(cmd[1]))
    } else if (cmd[0] === 'top') {
      console.log(stack.getTop());
    } else if (cmd[0] === 'pop') {
      console.log(stack.pop());
    } else if (cmd[0] === 'size') {
      console.log(stack.size());
    } else if (cmd[0] === 'empty') {
      console.log(stack.empty());
    }
  })
}

rl.on("line", (line) => {
  input.push(line)
})
  .on("close", () => {
    stackProcess(Number(input[0]), input.slice(1))
    process.exit()
  })