function groupAnagrams(strs: string[]): string[][] {
  const counter = new Map();

  for (let word of strs) {
    const sortedWord = Array.from(word).sort().toString();
    if (counter.has(sortedWord)) {
      counter.set(sortedWord, [...counter.get(sortedWord), word]);
    } else {
      counter.set(sortedWord, [word]);
    }
  }

  return Array.from(counter.values());
}
