function maxSubArray(nums: number[]): number {
  const dp = Array(nums.length).fill(0);
  dp[0] = nums[0];
  let maxSum = dp[0];

  for (let i = 1; i < nums.length; i++) {
    dp[i] = nums[i] + Math.max(dp[i - 1], 0);
    maxSum = Math.max(maxSum, dp[i]);
  }

  return maxSum;
}
