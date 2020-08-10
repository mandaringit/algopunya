const fs = require('fs');
const fileStream = fs.createReadStream('input.txt');
const readline = require('readline');

const rl = readline.createInterface({
  input: fileStream,
  output: process.stdout,
});

let input = [];

// 최소힙과 거의 비슷
class AbsHeap {
  constructor() {
    this.heap = [null];
    this.length = 0;
  }

  swap(i1, i2) {
    const temp = this.heap[i1];
    this.heap[i1] = this.heap[i2];
    this.heap[i2] = temp;
  }

  swapLeft(i) {
    this.swap(i, i * 2);
    return i * 2;
  }

  swapRight(i) {
    this.swap(i, i * 2 + 1);
    return i * 2 + 1;
  }

  insertion(X) {
    this.heap.push(X);
    this.length++;

    let childIdx = this.length;
    let parentIdx = Math.floor(childIdx / 2);

    // 절댓값이 더 작으면 계속 돌자
    while (childIdx !== 1 && Math.abs(X) <= Math.abs(this.heap[parentIdx])) {
      if (Math.abs(this.heap[parentIdx]) === Math.abs(X)) {
        // 절대값이 같으면 실제 크기중 작은놈을 올림
        if (this.heap[parentIdx] < Math.abs(X)) break;
      }
      this.swap(childIdx, parentIdx);
      childIdx = parentIdx;
      parentIdx = Math.floor(childIdx / 2);
    }
  }

  deletion() {
    if (this.length === 0) return 0;

    // 맨 마지막과 교환
    this.swap(1, this.length);
    // 빼면 그게 루트값
    const root = this.heap.pop();
    this.length--;

    //중간작업
    let i = 1;
    while (i < this.length) {
      const realCurr = this.heap[i];
      const realLeft = this.heap[i * 2];
      const realRight = this.heap[i * 2 + 1];
      const absCurr = Math.abs(this.heap[i]);
      const absLeft = Math.abs(this.heap[i * 2]);
      const absRight = Math.abs(this.heap[i * 2 + 1]);

      // 왼쪽이 없을 때는 그냥 둔다.
      if (!absLeft) break;
      // 오른쪽만 없을때는,
      else if (!absRight) {
        // 절대값 왼쪽이 절대값 현재값보다 작을때는 교환
        if (absLeft < absCurr) i = this.swapLeft(i);
        // 절대값이 같다면, 실제 값으로 비교해 왼쪽값이 작으면 교환.
        else if (absLeft === absCurr && realLeft < realCurr)
          i = this.swapLeft(i);
        else break;
      }
      // 왼쪽, 오른쪽 둘 다 있을때는,
      else {
        // 절댓값이 둘다 현재값보다 작으면
        if (absLeft < absCurr && absRight < absCurr) {
          if (absLeft === absRight) {
            // 절댓값이 가장 작은 수가 여러개일 때는,가장 작은수를 출력 및 제거
            if (realLeft <= realRight) i = this.swapLeft(i);
            else i = this.swapRight(i);
          } else if (absLeft < absRight) {
            i = this.swapLeft(i);
          } else if (absRight < absLeft) {
            this.swapRight(i);
          } else break;
        } else if (absLeft < absCurr) {
          i = this.swapLeft(i);
        } else if (absRight < absCurr) {
          i = this.swapRight(i);
        } else if (absLeft === absCurr && absRight === absCurr) {
          if (realLeft === realRight && realLeft < realCurr)
            i = this.swapLeft(i);
          else if (realLeft < realRight && realLeft < realCurr)
            i = this.swapLeft(i);
          else if (realRight > realLeft && realRight < realCurr)
            i = this.swapRight(i);
          else break;
        } else {
          break;
        }
      }
    }

    return root;
  }
}

rl.on('line', (line) => {
  input.push(parseInt(line));
}).on('close', () => {
  const absHeap = new AbsHeap();
  let result = '';
  input.slice(1).forEach((num) => {
    console.log('입--->', num);
    console.log(absHeap.heap);
    num === 0 ? (result += absHeap.deletion() + '\n') : absHeap.insertion(num);
    console.log(absHeap.heap);
    console.log('-----');
  });
  console.log(result);
  process.exit();
});
