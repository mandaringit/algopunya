/**
 * @param {number[]} nums
 * @return {number}
 */
var findNumbers = function (nums) {
  let total = 0;
  for (let i = 0; i < nums.length; i++) {
    const digitCount = nums[i].toString().length;
    digitCount % 2 === 0 && total++;
  }
  return total;
};
