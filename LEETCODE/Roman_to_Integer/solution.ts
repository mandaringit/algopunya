interface Roman {
  [char: string]: number;
}

function isSubtract(r1: string, r2: string): boolean {
  const case1 = r1 === "I" && "VX".includes(r2);
  const case2 = r1 === "X" && "LC".includes(r2);
  const case3 = r1 === "C" && "DM".includes(r2);

  return case1 || case2 || case3;
}

function romanToInt(s: string): number {
  const roman: Roman = {
    I: 1,
    V: 5,
    X: 10,
    L: 50,
    C: 100,
    D: 500,
    M: 1000,
  };

  let i = 0;
  let total = 0;

  while (i < s.length) {
    const numeral = s[i];

    if (["I", "X", "C"].includes(numeral) && i + 1 < s.length) {
      const n = s[i + 1];
      if (isSubtract(numeral, n)) {
        total += roman[n] - roman[numeral];
        i += 2;
      } else {
        total += roman[numeral];
        i++;
      }
    } else {
      total += roman[numeral];
      i++;
    }
  }

  return total;
}
