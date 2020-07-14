export const split = (str: string, delim: string = ''): string[] =>
  str.split(delim);

export const join = (strArray: string[], delim: string = ''): string =>
  strArray.join(delim);

console.log(split('hello'), split('h_e_l_l_o', '_'));
console.log(
  join(['h', 'e', 'l', 'l', 'o']),
  join(['h', 'e', 'l', 'l', 'o'], '_')
);
