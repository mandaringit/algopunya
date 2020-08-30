/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaxConsecutiveOnes = function (nums) {
  let maxCount = 0;
  let currentCount = 0;
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] === 1) {
      currentCount++;
      if (i === nums.length - 1) {
        maxCount = currentCount > maxCount ? currentCount : maxCount;
      }
    } else if (nums[i] === 0) {
      maxCount = currentCount > maxCount ? currentCount : maxCount;
      currentCount = 0;
    }
  }

  return maxCount;
};
