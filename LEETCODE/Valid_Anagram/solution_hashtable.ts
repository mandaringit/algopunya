interface Counter {
  [char: string]: number;
}

function isAnagram(s: string, t: string): boolean {
  const counter: Counter = {};

  for (let char of s) {
    if (counter.hasOwnProperty(char)) {
      counter[char]++;
    } else {
      counter[char] = 1;
    }
  }

  for (let char of t) {
    if (counter.hasOwnProperty(char) && counter[char] >= 1) {
      counter[char] -= 1;
    } else {
      return false;
    }
  }

  for (let char in counter) {
    if (counter[char] > 0) return false;
  }

  return true;
}
