function generate(
  left: number,
  right: number,
  form: string[],
  result: string[]
): void {
  if (left == 0 && right == 0) {
    result.push(form.join(""));
  } else if (left == right) {
    generate(left - 1, right, [...form, "("], result);
  } else if (left < right) {
    if (left > 0) generate(left - 1, right, [...form, "("], result);
    generate(left, right - 1, [...form, ")"], result);
  }
}

function generateParenthesis(n: number): string[] {
  const result = [];
  generate(n, n, [], result);
  return result;
}
