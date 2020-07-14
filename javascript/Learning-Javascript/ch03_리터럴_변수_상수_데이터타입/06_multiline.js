// 효과 없음
const multiline1 = "line1\
line2";
console.log(multiline1);

const multiline2 = "line1\n" +
    "\line2";
console.log(multiline2);

const multiline3 = `line1
line2`;
console.log(multiline3);

// 비추
const multiline4 = `line1
    line2
    line3`;
console.log(multiline4);

// 이하 추천
const multiline5 = "line1\n" +
    "line2\n" +
    "line3";
console.log(multiline5);

// 모두 혼합 가능
let currentTemp = 22.5;
const multiline6 = "Current temperature:\n" +
    `\t${currentTemp}\u00b0C\n` +
    "Don't worry ... the heat is on!";
console.log(multiline6);
