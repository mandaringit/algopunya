function missingNumber(nums: number[]): number {
  let missing = 0;
  for (let i = 1; i <= nums.length; i++) {
    missing ^= i; // 1 ~ N까지 XOR로 추가.
    missing ^= nums[i - 1]; // nums의 수를 XOR로 추가.
  }

  return missing;
}
