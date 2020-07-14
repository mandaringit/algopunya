const addhof = (a: number): ((number) => number) => (b: number): number =>
  a + b;
const result2 = addhof(1)(2);
console.log(result2);
