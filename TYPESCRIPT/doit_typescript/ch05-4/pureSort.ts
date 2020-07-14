export const pureSort = <T>(array: readonly T[]): T[] => {
  const copiedArray = [...array];
  return copiedArray.sort();
};
