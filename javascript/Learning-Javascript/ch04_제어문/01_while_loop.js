let funds = 50;

// 기본적인 while문 구조
while (funds > 1 && funds < 100) {
    funds = funds + 2;
}

// 블록 문 (block statement)
{
    console.log("statement1");
    console.log("statement2");
} // 블록 문 종료

console.log("statement3");

// 공백 (이런식은 비추입니다.)
while (funds > 1 && funds < 100)

funds = funds+2;

// 줄바꿈 없음
while (funds >1 && funds <100) funds = funds + 2;
while (funds > 1 && funds < 100){ funds = funds + 2; }
