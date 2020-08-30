/**
 * @param {number[]} arr
 * @return {void} Do not return anything, modify arr in-place instead.
 */
var duplicateZeros = function (arr) {
  let i = 0;
  while (i < arr.length) {
    if (arr[i] === 0) {
      // 정렬하려고 하는 부분이 모두 0인지 확인해보고 넘어감
      const partSum = arr.slice(i).reduce((acc, curr) => acc + curr, 0);
      if (partSum === 0) break;

      // 뒤부터 한칸씩 앞과 교체
      for (let j = arr.length - 1; j > i + 1; j--) {
        arr[j] = arr[j - 1];
      }

      // 마지막 인덱스가 아닌 경우만 0 다음을 0으로 교체 & 인덱스 이동
      if (i < arr.length - 1) {
        arr[i + 1] = 0;
        i = i + 2;
      }
    } else {
      i++;
    }
  }
};
