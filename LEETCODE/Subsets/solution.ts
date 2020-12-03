function subsets(nums: number[]): number[][] {
  const result = [];

  const generateSubset = (path: number[], count: number) => {
    if (count === 0) {
      result.push(path);
      return;
    }
    generateSubset(path, count - 1);
    generateSubset([nums[count - 1], ...path], count - 1);
  };

  generateSubset([], nums.length);

  return result;
}
