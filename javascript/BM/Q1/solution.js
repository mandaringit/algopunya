function solution(arr) {
  let count = 0;

  function zipping(numbers) {
    if (numbers.toString() === "1") {
      return 'done'
    } else {
      count += 1;
      // 줄이는 작업
      let newNumbers = [];
      let sameCount = 1;
      let prevNumber = numbers[0];
      for (let i = 1; i < numbers.length; i++) {
        const selectedNumber = numbers[i];
        if (prevNumber === selectedNumber) {
          sameCount += 1;
          prevNumber = selectedNumber;
        } else {
          newNumbers.push(sameCount);
          sameCount = 1;
          prevNumber = selectedNumber;
        }
      }
      newNumbers.push(sameCount);

      console.log(newNumbers);
      zipping(newNumbers)
    }
  }

  zipping(arr);
  return count;
}

solution([1, 2, 3])