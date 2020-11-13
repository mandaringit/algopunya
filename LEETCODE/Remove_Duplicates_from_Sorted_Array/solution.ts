function removeDuplicates(nums: number[]): number {
  if (nums.length <= 1) return nums.length;

  let slow = 0;
  for (let fast = 1; fast < nums.length; fast++) {
    if (nums[slow] < nums[fast]) {
      slow += 1;
      const temp = nums[slow];
      nums[slow] = nums[fast];
      nums[fast] = temp;
    }
  }

  return slow + 1;
}
