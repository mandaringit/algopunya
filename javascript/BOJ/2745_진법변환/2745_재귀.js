const fs = require('fs');
const fileStream = fs.createReadStream('input.txt');
const readline = require('readline');

const rl = readline.createInterface({
  input: fileStream,
  output: process.stdout,
})

let N = null; // B진법 수 N
let B = null; // B진법

/**
 * '0' ~ '9' => 48 ~ 57
 * 'A' ~ 'Z' => 65 ~ 90
 */
// 자릿수, 결과값
function conversion(place, result) {
  if (B === 10) return N;
  const charPlace = N.length - place - 1 // 변환할 문자 위치는 뒤에서부터..!
  const charAscii = N[charPlace].charCodeAt(0);
  const cNum = charAscii >= 48 && charAscii <= 57 ? Number(N[charPlace]) : Number(charAscii) - 55;
  result += cNum * Math.pow(B, place);
  place++;
  if (place === N.length) return result;
  return conversion(place, result);
}


rl.on("line", (line) => {
  [N, B] = line.split(" ");
  B = Number(B);
})
  .on("close", () => {
    console.log(conversion(0, 0));
    process.exit()
  })
