function rob(nums: number[]): number {
  let prev1 = 0;
  let prev2 = 0;

  for (let num of nums) {
    const now = Math.max(num + prev2, prev1);
    prev2 = prev1;
    prev1 = now;
  }

  return prev1;
}
