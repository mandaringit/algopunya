/**
 * @param {number[]} A
 * @return {number[]}
 */
var sortedSquares = function (A) {
  return A.map((num) => num * num).sort((a, b) => a - b);
};
