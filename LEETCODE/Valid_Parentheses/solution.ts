function isValid(s: string): boolean {
  const stack = [];
  const pair = new Map([
    ["(", ")"],
    ["[", "]"],
    ["{", "}"],
  ]);

  for (let bracket of s) {
    if (pair.has(bracket)) {
      stack.push(bracket);
    } else if (
      stack.length > 0 &&
      pair.get(stack[stack.length - 1]) === bracket
    ) {
      stack.pop();
    } else {
      return false;
    }
  }

  return stack.length === 0;
}
