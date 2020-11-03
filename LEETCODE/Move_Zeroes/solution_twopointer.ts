/**
 Do not return anything, modify nums in-place instead.
 */
function moveZeroes(nums: number[]): void {
  let slow = 0;
  for (let fast = 0; fast < nums.length; fast++) {
    if (nums[fast] !== 0) {
      const temp = nums[fast];
      nums[fast] = nums[slow];
      nums[slow] = temp;
    }

    if (nums[slow] !== 0) slow++;
  }
}
