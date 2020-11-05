function generate(numRows: number): number[][] {
  const pascal = [];

  for (let i = 0; i < numRows; i++) {
    if (i === 0) pascal.push([1]);
    else {
      const row = [1];
      for (let j = 0; j < i - 1; j++) {
        row.push(pascal[i - 1][j] + pascal[i - 1][j + 1]);
      }
      row.push(1);
      pascal.push(row);
    }
  }

  return pascal;
}
