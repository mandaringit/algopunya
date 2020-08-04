function solution(numbers, target) {
  let answer = 0;

  function isTargetNumber(current, count) {
    if (count === numbers.length) {
      if (current === target) {
        answer += 1
      }
    } else {
      isTargetNumber(current + numbers[count], count + 1);
      isTargetNumber(current - numbers[count], count + 1);
    }
  }

  isTargetNumber(0, 0);

  return answer;
}

console.log(solution([1,1,1,1,1],3));