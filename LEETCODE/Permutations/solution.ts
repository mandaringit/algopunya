function dfs(nums: number[], path: number[], result: number[][]): void {
  if (nums.length === 0) {
    result.push(path);
  }

  for (let i = 0; i < nums.length; i++) {
    dfs(
      [...nums.slice(0, i), ...nums.slice(i + 1, nums.length)],
      [...path, nums[i]],
      result
    );
  }
}

function permute(nums: number[]): number[][] {
  const result = [];

  dfs(nums, [], result);

  return result;
}
