const fs = require('fs');
const fileStream = fs.createReadStream('input.txt');
const readline = require('readline');

const rl = readline.createInterface({
  input: fileStream,
  output: process.stdout,
});

let input = [];

class MinHeap {
  constructor() {
    this.heap = [null];
    this.length = 0;
  }

  swap(i1, i2) {
    const temp = this.heap[i1];
    this.heap[i1] = this.heap[i2];
    this.heap[i2] = temp;
  }

  insertion(X) {
    // 일단 맨 뒤에 넣는다.
    this.heap.push(X);
    this.length++;

    let childIdx = this.length;
    let parentIdx = Math.floor(childIdx / 2);

    while (childIdx !== 1 && X < this.heap[parentIdx]) {
      this.swap(childIdx, parentIdx);

      // 인덱스도 바꿈
      childIdx = parentIdx;
      parentIdx = Math.floor(childIdx / 2);
    }
  }

  deletion() {
    if (this.length === 0) return 0; // 없을때 0 리턴

    // 맨앞 - 맨뒤 교환
    this.swap(1, this.length);
    const root = this.heap.pop();
    this.length--;

    let i = 1;
    while (i < this.length) {
      const curr = this.heap[i];
      const left = this.heap[2 * i];
      const right = this.heap[2 * i + 1];

      // 아무것도 없을때
      if (!left) break;

      // 왼쪽만 있을때
      if (!right) {
        if (left < curr) {
          this.swap(i, 2 * i);
          i = 2 * i;
        } else {
          break;
        }
      } else {
        // 둘 다 있을때
        if (left < curr && right < curr) {
          if (left < right) {
            this.swap(i, 2 * i);
            i = 2 * i;
          } else {
            this.swap(i, 2 * i + 1);
            i = 2 * i + 1;
          }
        } else if (left < curr) {
          this.swap(i, 2 * i);
          i = 2 * i;
        } else if (right < curr) {
          this.swap(i, 2 * i + 1);
          i = 2 * i + 1;
        }
      }
    }

    return root;
  }
}

rl.on('line', (line) => {
  input.push(parseInt(line));
}).on('close', () => {
  const minHeap = new MinHeap();
  let result = '';
  for (let num of input.slice(1)) {
    if (num === 0) result += minHeap.deletion() + '\n';
    else minHeap.insertion(num);
  }
  console.log(result);
  process.exit();
});
