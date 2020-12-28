/**
 * 시간 O(N) + 공간 O(N)
 */
function findDisappearedNumbers(nums: number[]): number[] {
  const counter = Array(nums.length + 1).fill(0);

  for (let i = 0; i < nums.length; i++) {
    counter[nums[i]]++;
  }

  const result = [];

  for (let i = 1; i < nums.length + 1; i++) {
    if (counter[i] === 0) result.push(i);
  }

  return result;
}
