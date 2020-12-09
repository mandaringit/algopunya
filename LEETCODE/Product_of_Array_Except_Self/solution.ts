function productExceptSelf(nums: number[]): number[] {
  const N = nums.length;
  const result = Array(N).fill(1);

  let p = 1;
  for (let i = 0; i < N; i++) {
    result[i] = result[i] * p;
    p = p * nums[i];
  }

  p = 1;
  for (let i = N - 1; i >= 0; i--) {
    result[i] = result[i] * p;
    p = p * nums[i];
  }

  return result;
}
