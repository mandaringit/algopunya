function firstUniqChar(s: string): number {
  const characters: { [char: string]: [boolean, number] } = {};

  for (let i = 0; i < s.length; i++) {
    const char = s[i];
    if (characters.hasOwnProperty(char)) {
      characters[char][0] = true;
    } else {
      characters[char] = [false, i];
    }
  }

  for (let char in characters) {
    if (!characters[char][0]) {
      return characters[char][1];
    }
  }

  return -1;
}
