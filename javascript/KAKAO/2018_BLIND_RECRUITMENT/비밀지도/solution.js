function solution(n, arr1, arr2) {

  function getBinaryMap(arr) {
    let binaryMap = [];

    for (let value of arr) {
      let binaryValue = value.toString(2);
      let paddedValue = binaryValue.padStart(n, '0');
      binaryMap.push(paddedValue);
    }

    return binaryMap
  }

  let map1 = getBinaryMap(arr1);
  let map2 = getBinaryMap(arr2);

  let originalMap = [];
  for (let i = 0; i < n; i++) {
    let line = '';
    for (let j = 0; j < n; j++) {
      let map1Value = map1[i][j];
      let map2Value = map2[i][j];

      if (map1Value === '0' && map2Value === '0') {
        line += ' ';
      } else {
        line += '#';
      }
    }
    originalMap.push(line);
  }
  return originalMap
}


module.exports = solution;