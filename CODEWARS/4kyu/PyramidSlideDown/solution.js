function longestSlideDown(pyramid) {
  for (let i = 1; i < pyramid.length; i++) {
    for (let j = 0; j < pyramid[i].length; j++) {
      const left = j === 0 ? 0 : pyramid[i - 1][j - 1];
      const right = j === pyramid[i].length - 1 ? 0 : pyramid[i - 1][j];
      pyramid[i][j] = pyramid[i][j] + Math.max(left, right);
    }
  }
  return pyramid[pyramid.length - 1].reduce((prev, curr) => Math.max(prev, curr))
}

console.log(longestSlideDown([[3],
  [7, 4],
  [2, 4, 6],
  [8, 5, 9, 3]]))