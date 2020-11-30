function reverse(x: number): number {
  const strX = Math.abs(x).toString();
  const rev = [];

  for (let i = strX.length - 1; i >= 0; i--) {
    rev.push(strX[i]);
  }

  const revX = x > 0 ? parseInt(rev.join("")) : -parseInt(rev.join(""));

  return revX < Math.pow(2, 31) && revX > -Math.pow(2, 31) ? revX : 0;
}
