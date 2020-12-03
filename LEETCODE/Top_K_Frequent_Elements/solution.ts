function topKFrequent(nums: number[], k: number): number[] {
  const counter = new Map();

  nums.forEach((num) => counter.set(num, counter.get(num) + 1 || 1));

  const sortedArr = [...counter.entries()].sort((a, b) => b[1] - a[1]);

  const result = [];
  for (let i = 0; i < k; i++) {
    result.push(sortedArr[i][0]);
  }
  return result;
}
