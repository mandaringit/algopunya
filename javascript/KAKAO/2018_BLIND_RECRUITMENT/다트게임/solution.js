function solution(dartResult) {
  let results = ['', '', ''];
  let scores = [0, 0, 0];
  let stage = 0;

  for (let i = 0; i < dartResult.length; i++) {
    const char = dartResult[i];
    if ('SDT'.includes(char)) {
      results[stage] = results[stage] + char;
      stage += 1;
    } else if ("#*".includes(char)) {
      results[stage - 1] = results[stage - 1] + char;
    } else {
      results[stage] = results[stage] + char
    }
  }
  const areas = {
    S: 1,
    D: 2,
    T: 3,
  };

  for (let i = 0; i < results.length; i++) {
    const result = results[i];
    let basicScore = '';
    let area = '';
    let option = '';

    for (let char of result) {
      if (Number.isInteger(Number(char))) {
        basicScore += char;
      } else if ('SDT'.includes(char)) {
        area = char;
      } else {
        option = char;
      }
      scores[i] = parseInt(basicScore) ** areas[area];

      if (option) {
        if (option === '*') {
          if (i > 0) {
            scores[i - 1] = scores[i - 1] * 2
          }
          scores[i] = scores[i] * 2
        } else if (option === '#') {
          scores[i] = -scores[i]
        }
      }
    }
  }
  return scores.reduce((prev, curr) => prev += curr, 0)
}

module.exports = solution;