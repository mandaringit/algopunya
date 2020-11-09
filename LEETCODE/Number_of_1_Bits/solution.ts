function hammingWeight(n: number): number {
  const bin = n.toString(2);
  let count = 0;
  for (let bit of bin) {
    if (bit === "1") count++;
  }
  return count;
}

function hammingWeight2(n: number): number {
  let count = 0;
  while (n !== 0) {
    n &= n - 1;
    count++;
  }
  return count;
}
