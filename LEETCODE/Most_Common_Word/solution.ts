function mostCommonWord(paragraph: string, banned: string[]): string {
  const words = paragraph
    .replace(/[^\w]+/gi, " ")
    .trim()
    .toLowerCase()
    .split(" ")
    .filter((word) => !banned.includes(word));

  const counter = new Map<string, number>();
  let max: [number, string] = [0, null];
  words.forEach((word) => {
    counter.set(word, counter.has(word) ? counter.get(word) + 1 : 1);
    const count = counter.get(word);
    if (count > max[0]) {
      max = [count, word];
    }
  });

  return max[1];
}
