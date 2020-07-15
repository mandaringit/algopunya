function solution(heights) {
  let answer = [0];

  for (let i = 1; i < heights.length; i++) {
    for (let j = i - 1; j >= 0; j--) {
      const sending = heights[i];
      const received = heights[j];

      if (sending < received) {
        answer.push(j + 1);
        break;
      }

      if (j === 0 && sending >= received) {
        answer.push(0)
      }
    }
  }
  return answer;
}

solution([6, 9, 5, 7, 4]);
solution([3, 9, 9, 3, 5, 7, 2]);