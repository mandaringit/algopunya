const fs = require('fs');
const fileStream = fs.createReadStream('input.txt');
const readline = require('readline');

const rl = readline.createInterface({
  input: fileStream,
  output: process.stdout,
});

let input = [];

class Heap {
  constructor() {
    this.heap = [null]; // 보통 0번째는 빈 값으로 넣고 1부터 시작하도록 구현
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

    // 집어 넣은 요소의 위치가 맨 위가 아님 && 부모 요소보다 더 크다면 -> swap
    while (childIdx !== 1 && X > this.heap[parentIdx]) {
      // 교환
      this.swap(parentIdx, childIdx);
      // 교환 후 자식 인덱스의 위치는 부모 인덱스의 위치가 됨.
      childIdx = parentIdx;
      // 다음 비교할 부모 인덱스도 수정
      parentIdx = Math.floor(childIdx / 2);
    }
  }

  deletion() {
    // 만약 요소가 아무것도 없다면 0을 리턴.
    if (this.length === 0) return 0;

    // 첫번째와 마지막 요소를 바꾼다.
    this.swap(1, this.length);

    // 스왑한 첫번째 요소를 제거. = 우리가 리턴할 값.
    const root = this.heap.pop();
    this.length--;

    // 첫번째 자리부터 시작해서
    let i = 1;
    // 인덱스가 힙의 길이를 넘지 않을때까지 반복
    while (i < this.length) {
      let curr = this.heap[i]; // 기준 노드
      let left = this.heap[i * 2]; // 기준 노드의 왼쪽
      let right = this.heap[i * 2 + 1]; // 기준 노드의 오른쪽

      // 완전 이진 트리라는 것을 기억한다면..
      // 만약 왼쪽노드가 없다면 -> 더이상 바꿀 자식이 없다는것
      if (!left) break;

      // 오른쪽 노드만 없다면 대소 비교 시작후 스왑.
      if (!right) {
        if (curr < left) {
          this.swap(i, i * 2);
          i = i * 2;
        } else {
          break;
        }
      } else {
        // 왼쪽, 오른쪽 둘 다 있다면 둘 비교 후 큰쪽과 스왑.
        if (curr < left && curr < right) {
          if (left > right) {
            this.swap(i, i * 2);
            i = i * 2;
          } else {
            this.swap(i, i * 2 + 1);
            i = i * 2 + 1;
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

rl.on('line', (line) => {
  input.push(parseInt(line));
}).on('close', () => {
  const heap = new Heap();
  let result = '';
  for (let cmd of input.slice(1)) {
    if (cmd === 0) result += heap.deletion() + '\n';
    else heap.insertion(cmd);
  }
  console.log(result);
  process.exit();
});
