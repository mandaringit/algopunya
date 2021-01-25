function reorderLogFiles(logs: string[]): string[] {
  const letter_logs: string[] = [];
  const digit_logs: string[] = [];

  logs.forEach((log) => {
    if (Number.isNaN(Number(log.split(" ")[1]))) {
      letter_logs.push(log);
    } else {
      digit_logs.push(log);
    }
  });

  letter_logs.sort((a, b) => {
    const [idA, ...logA] = a.split(" ");
    const [idB, ...logB] = b.split(" ");

    if (logA.join(" ") > logB.join(" ")) {
      return 1;
    } else if (logA.join(" ") < logB.join(" ")) {
      return -1;
    } else {
      return idA > idB ? 1 : -1;
    }
  });

  return [...letter_logs, ...digit_logs];
}
