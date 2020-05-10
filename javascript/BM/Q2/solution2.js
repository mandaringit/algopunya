function solution(arr) {
  let anagramSet = new Set();
  for (let number of arr) {
    const separateNumber = {};

    const stringNumber = number.toString();

    for (let digit of stringNumber) {
      if (separateNumber[digit]) {
        separateNumber[digit] += 1
      } else {
        separateNumber[digit] = 1
      }
    }

    anagramSet.add(JSON.stringify(separateNumber))

  }
  return anagramSet.size;
}

solution([112, 1814, 121, 1481, 1184]);