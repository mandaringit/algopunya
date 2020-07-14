function getRainbowIterator() {
  const colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'];
  let colorIndex = -1;
  return {
    next() {
      if (++colorIndex >= colors.length) colorIndex = 0;
      return {value: colors[colorIndex], done: false}
    },
  }
}

function isLeapYear(year) {
  if (year % 4 !== 0) return false;
  else if (year % 100 !== 0) return true;
  else if (year % 400 !== 0) return false;
  else return true;
}