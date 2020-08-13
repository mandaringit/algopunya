const fs = require('fs');
const fileStream = fs.createReadStream('input.txt');
const readline = require('readline');

const rl = readline.createInterface({
  input: fileStream,
  output: process.stdout,
});

let input = [];

function solution(N, M, brands) {
  let price = 0;
  const quotient = Math.floor(N / 6);
  const remainder = N % 6;
  let cheapPack = 1000;
  let cheapPiece = 1000;
  for (let [pack, piece] of brands) {
    // 팩이 제일 싼놈, 단품이 제일 싼놈
    // 6개 이상일때는 팩 1개당 가격 & 단품 가격 중 싼걸로 다 채우고
    // 나머지는 각각의 단품 가격 * 개수 곱한뒤, 팩 가격보다 싸면 그걸로, 팩이 더 싸면 팩으로 비교
    cheapPack = pack < cheapPack ? pack : cheapPack;
    cheapPiece = piece < cheapPiece ? piece : cheapPiece;
  }

  // 6개 이상일때 처리
  if (quotient > 0) {
    // 팩이 개당보다 비쌀때
    if (cheapPack > cheapPiece * 6) {
      price += quotient * (cheapPiece * 6);
    } else {
      price += quotient * cheapPack;
    }
  }
  // 나머지 처리.  팩이 개당 * 나머지보다 비쌀때
  if (cheapPack > cheapPiece * remainder) {
    price += cheapPiece * remainder;
  } else {
    price += cheapPack;
  }

  return price;
}

rl.on('line', (line) => {
  input.push(line);
}).on('close', () => {
  const [N, M] = input[0].split(' ').map(Number);
  const brands = input.slice(1).map((brand) => brand.split(' ').map(Number));
  console.log(solution(N, M, brands));
  process.exit();
});
