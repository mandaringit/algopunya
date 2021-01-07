function partitionLabels(S: string): number[] {
  const rightMost = new Map();

  for (let i = 0; i < S.length; i++) {
    const char = S[i];
    rightMost.set(char, i);
  }

  let left = 0;
  let right = 0;
  const result = [];

  for (let i = 0; i < S.length; i++) {
    right = Math.max(right, rightMost.get(S[i]));

    if (i === right) {
      result.push(right - left + 1);
      left = i + 1;
    }
  }

  return result;
}
