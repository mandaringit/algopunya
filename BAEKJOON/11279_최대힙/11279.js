const fs = require('fs');
const fileStream = fs.createReadStream('input.txt');
const readline = require('readline');

const rl = readline.createInterface({
  input: fileStream,
  output: process.stdout,
})

let input = []

class Heap {
  constructor() {
    this.heap = [null]
  }

  swap(i1, i2) {
    const temp = this.heap[i1];
    this.heap[i1] = this.heap[i2];
    this.heap[i2] = temp;
  }

  push(X) {
    // 맨 뒤에 넣는다.
    this.heap.push(X);
    let childIdx = this.heap.length - 1;
    let parentIdx = Math.floor(childIdx / 2);
    // 자신이 부모보다 크다면 계속해서..
    while (childIdx !== 1 && X > this.heap[parentIdx]) {
      // 교환
      this.swap(parentIdx, childIdx);
      childIdx = parentIdx;
      parentIdx = Math.floor(childIdx / 2);
    }
  }

  del() {
    if (this.heap.length - 1 === 0) return 0;
    this.swap(1,this.heap.length-1);
    // 마지막 요소를 제거해 제일 앞 요소와 바꾼다.
    const root = this.heap.pop();
    let i = 1;
    while (i < this.heap.length - 1) {
      let left = this.heap[i * 2];
      let right = this.heap[i * 2 + 1];
      let curr = this.heap[i]
      if (!left) break;
      if (!right) {
        if (curr < left) {
          this.swap(i, i * 2);
          i = i * 2;
        } else {
          break;
        }
      } else {
        if (curr < left && curr < right) {
          if (left > right) {
            this.swap(i, i * 2);
            i = i * 2
          } else {
            this.swap(i, i * 2 + 1)
            i = i * 2 + 1
          }
        } else if (curr < left) {
          this.swap(i, i * 2);
          i = i * 2;
        } else if (curr < right) {
          this.swap(i, i * 2 + 1);
          i = i * 2 + 1;
        } else {
          break;
        }

      }
    }


    return root;
  }
}

rl.on("line", (line) => {
  input.push(parseInt(line));
})
  .on("close", () => {
    const heap = new Heap();
    for (let cmd of input.slice(1)) {
      if (cmd === 0) console.log(heap.del())
      else heap.push(cmd)
    }
    process.exit()
  })