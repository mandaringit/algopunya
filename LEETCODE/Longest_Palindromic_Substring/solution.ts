function longestPalindrome(s: string): string {
  if (s.length < 2 || s.split("").reverse().join("") === s) {
    return s;
  }

  const expand = (left: number, right: number): string => {
    while (left >= 0 && right < s.length && s[left] === s[right]) {
      left -= 1;
      right += 1;
    }
    return s.slice(left + 1, right);
  };

  let result = "";
  for (let i = 0; i < s.length; i++) {
    const oddSlide = expand(i, i + 1);
    const evenSlide = expand(i, i + 2);

    if (oddSlide.length >= evenSlide.length) {
      result = oddSlide.length > result.length ? oddSlide : result;
    } else {
      result = evenSlide.length > result.length ? evenSlide : result;
    }
  }

  return result;
}
