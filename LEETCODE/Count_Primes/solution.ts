function countPrimes(n: number): number {
  if (n < 3) return 0;

  const isPrime = Array(n).fill(true);
  isPrime[0] = isPrime[1] = false;

  let primeCount = 0;
  for (let i = 2; i < n; i++) {
    if (isPrime[i]) {
      primeCount++;
      for (let j = i + i; j < n; j += i) {
        isPrime[j] = false;
      }
    }
  }
  return primeCount;
}
