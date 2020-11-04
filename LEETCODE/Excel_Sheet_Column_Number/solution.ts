function titleToNumber(s: string): number {
  let num = 0;
  for (let char of s) {
    num = num * 26 + char.charCodeAt(0) - 64;
  }
  return num;
}
