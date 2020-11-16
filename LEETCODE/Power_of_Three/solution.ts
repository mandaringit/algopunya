function isPowerOfThree(n: number): boolean {
  return n > 0 && !(Math.pow(3, 20) % n);
}
