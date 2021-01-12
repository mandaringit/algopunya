function dailyTemperatures(T: number[]): number[] {
  const result = Array(T.length).fill(0);
  const stack = [];

  for (let i = 0; i < T.length; i++) {
    const t = T[i];
    while (stack.length > 0 && T[stack[stack.length - 1]] < t) {
      const prevIdx = stack.pop();
      const d = i - prevIdx;
      result[prevIdx] = d;
    }
    stack.push(i);
  }

  return result;
}
