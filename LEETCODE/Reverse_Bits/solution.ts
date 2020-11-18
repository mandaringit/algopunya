function reverseBits(n: number): number {
  let ans = 0;
  let count = 32;

  while (count--) {
    ans *= 2;
    ans += n & 1;
    n = n >> 1;
  }

  return ans;
}
