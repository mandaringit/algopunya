const fs = require('fs');
const fileStream = fs.createReadStream('input.txt');
const readline = require('readline');

const rl = readline.createInterface({
  input: fileStream,
  output: process.stdout,
})

let input = []

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
    this.rear += 1
  }

  pop() {
    if (!this.empty()) {
      const value = this.queue[this.front];
      this.front++;
      return value;
    }
    return -1
  }

  size() {
    return this.rear - this.front;
  }

  getFront() {
    return this.empty() ? -1 : this.queue[this.front];
  }

  getRear() {
    return this.empty() ? -1 : this.queue[this.rear-1];
  }
}

function queueProcess(N,input){
  const queue = new Queue(N);
  input.forEach(cmds => {
    const cmd =  cmds.split(" ");
    if(cmd[0] === 'push') {
      queue.push(cmd[1]);
    } else if(cmd[0] === 'pop') {
      console.log(queue.pop());
    } else if (cmd[0] === 'size'){
      console.log(queue.size());
    } else if(cmd[0] === 'empty'){
      console.log(queue.empty());
    } else if(cmd[0] === 'front'){
      console.log(queue.getFront());
    } else if(cmd[0] === 'back'){
      console.log(queue.getRear());
    }
  })
}

rl.on("line", (line) => {
  input.push(line);
})
  .on("close", () => {
    queueProcess(Number(input[0]),input.slice(1))
    process.exit()
  })