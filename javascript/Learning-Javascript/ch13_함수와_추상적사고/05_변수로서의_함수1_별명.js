function addThreeSquareAddFiveTakeSquareRoot(x) {
  // 설마 이런 이름을 짓지는 않겠지만 ..
  return Math.sqrt(Math.pow(x + 3, 2) + 2);
}

// 별명 쓰기 전
const answer = (addThreeSquareAddFiveTakeSquareRoot(5)
  + addThreeSquareAddFiveTakeSquareRoot(2)) /
  addThreeSquareAddFiveTakeSquareRoot(7);

// 별명 쓴 이후
const f = addThreeSquareAddFiveTakeSquareRoot;
const answer2 = (f(5) + f(2)) / f(7);

const money = require('math-money');

const oneDollar = Money.Dollar(1);

// Money.Dollar도 길면 이렇게 쓰자
const Dollar = Money.Dollar;
const twoDollar = Dollar(2);
