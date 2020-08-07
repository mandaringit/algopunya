const fs = require('fs');
const fileStream = fs.createReadStream('input.txt');
const readline = require('readline');

const rl = readline.createInterface({
  input: fileStream,
  output: process.stdout,
});

let input = [];

class Queue {
  constructor(N) {
    this.queue = Array(N).fill(0);
    this.front = 0;
    this.rear = 0;
  }

  empty() {
    return this.front === this.rear ? 1 : 0;
  }

  push(X) {
    this.queue[this.rear] = X;
    this.rear += 1;
  }

  pop() {
    if (!this.empty()) {
      const value = this.queue[this.front];
      this.front++;
      return value;
    }
    return -1;
  }

  size() {
    return this.rear - this.front;
  }

  getFront() {
    return this.empty() ? -1 : this.queue[this.front];
  }

  getRear() {
    return this.empty() ? -1 : this.queue[this.rear - 1];
  }
}

function queueProcess(N, input) {
  const queue = new Queue(N);
  let result = '';
  input.forEach((cmds) => {
    const cmd = cmds.split(' ');
    if (cmd[0] === 'push') {
      queue.push(cmd[1]);
    } else if (cmd[0] === 'pop') {
      result += queue.pop() + '\n';
    } else if (cmd[0] === 'size') {
      result += queue.size() + '\n';
    } else if (cmd[0] === 'empty') {
      result += queue.empty() + '\n';
    } else if (cmd[0] === 'front') {
      result += queue.getFront() + '\n';
    } else if (cmd[0] === 'back') {
      result += queue.getRear() + '\n';
    }
  });
  return result;
}

rl.on('line', (line) => {
  input.push(line);
}).on('close', () => {
  console.log(queueProcess(Number(input[0]), input.slice(1)));
  process.exit();
});
