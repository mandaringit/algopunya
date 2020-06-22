// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

// 배열에서, 감소 -> 증가 또는 증가 -> 감소 구간 찾기.
// 처음, 또는 마지막의 경우 그냥 지어줌
//

function solution(A) {
  if (A.length === 2) {
    return A[0] === A[1] ? 1 : 2
  } else {
    let count = 0
    let idx = 1;
    while (idx < A.length - 1) {
      const l = A[idx - 1];
      const c = A[idx];
      let r = A[idx + 1];
      let nextIdx = idx + 1;
      while (nextIdx !== A.length - 1 && c === r) {
        nextIdx += 1;
        r = A[nextIdx];
        idx = nextIdx - 1;
      }
      if (l < c && c > r) {
        idx = nextIdx
        count += 1
      } else if (l > c && c < r) {
        idx = nextIdx;
        count += 1
      } else {
        idx += 1
      }
    }
    return count + 2;
  }
}

console.log(solution([2, 2, 3, 4, 3, 3, 2, 2, 1, 1, 2, 5]))
console.log(solution([3, 2, 3, 2, 3, 2, 3, 2]))
console.log(solution([3, 2, 2, 2, 2, 2, 2, 3]))


