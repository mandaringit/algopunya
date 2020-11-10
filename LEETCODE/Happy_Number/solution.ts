function digitSum(n: number): number {
  let result = 0;
  while (n) {
    const r = n % 10; // 나머지
    n = Math.trunc(n / 10);
    result += Math.pow(r, 2);
  }
  return result;
}

function isHappy(n: number): boolean {
  let slow = n;
  let fast = n;
  do {
    slow = digitSum(slow);
    fast = digitSum(digitSum(fast));
  } while (slow !== fast);
  return fast === 1;
}
