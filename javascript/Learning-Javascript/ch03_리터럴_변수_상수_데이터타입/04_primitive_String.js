// 문자열은 텍스트 데이터다.
// 자바스크립트 문자열은 유니코드 텍스트다.

// 이스케이프가 필요 없는 경우
const dialog = 'Sam looked up, and said "hello,old friend!", as Max walked in.';
const imperative = "Don't do that!";
console.log(dialog, imperative);

// 이스케이프가 필요한 경우
// const dialog2 = "Sam looked up and said "dont't do that!" to Max.";   // error
const dialog2 = "Sam looked up and said \"dont't do that!\" to Max.";
const dialog3 = 'He looked up and said "don\'t do that!" to Max.';
const s = 'In Javascript, use \\ as an escape character in strings.';
console.log(dialog2, dialog3, s);

// 특수문자
const newline = "Line1\nLine2";
console.log(newline);
const carriageReturn = "Windows line 1\r\nWindows lien 2"; // \r 옆을 싹 밀어버림 옛날 타자기 생각
console.log(carriageReturn);
const tap = "Speed:\t60kph";
console.log(tap);
const small = "Don\'t";
console.log(small);
const big = 'Sam said \"hello\".';
console.log(big);
const backtick = `New in ES6: \` string`;
console.log(backtick);
const dollar = `New in ES6: ${small}`;
console.log(dollar);
const reverse_slash = "Use \\\\ to represent\\!";
console.log(reverse_slash);
const unicode_point = "De Morgan's law: \u2310(P \u22c0Q) \u21D4 (\u2310P) \u2310Q)";
console.log(unicode_point);
const latin_1 = "\xc9p\xe9e is fun , but foil is more fun";
console.log(latin_1);


