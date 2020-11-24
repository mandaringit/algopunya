function isAlnum(char: string): boolean {
  const charCode = char.charCodeAt(0);
  if (charCode >= 48 && charCode <= 57) return true; // 0 - 9
  if (charCode >= 65 && charCode <= 90) return true; // a-z
  if (charCode >= 97 && charCode <= 122) return true; // A-Z
  return false;
}

function isPalindrome(s: string): boolean {
  if (s === "") return true;

  let left = 0;
  let right = s.length - 1;

  while (left < right) {
    if (isAlnum(s[left]) && isAlnum(s[right])) {
      if (s[left].toLowerCase() === s[right].toLowerCase()) {
        left++;
        right--;
      } else {
        return false;
      }
    } else {
      if (!isAlnum(s[left])) left++;
      if (!isAlnum(s[right])) right--;
    }
  }

  return true;
}
