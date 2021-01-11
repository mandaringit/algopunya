function reconstructQueue(people: number[][]): number[][] {
  people.sort((a, b) => {
    if (a[0] === b[0]) {
      return a[1] - b[1];
    }
    return b[0] - a[0];
  });

  let result = [];

  for (let p of people) {
    const [_, k] = p;
    result.splice(k, 0, p);
  }

  return result;
}
