export const fold = <T>(
  array: T[],
  callback: (result: T, val: T) => T,
  initValue: T
): T => {
  let result: T = initValue;
  for (let i = 0; i < array.length; i++) {
    const value: T = array[i];
    result = callback(result, value);
  }
  return result;
};
