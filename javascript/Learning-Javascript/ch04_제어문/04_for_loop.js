// 기본 모양
// for ([initialization];[condition];[final-expression])
//     statement

// for loop의 다른 패턴들.
for (let temp, i = 0, j = 1; j < 30; temp = i, i = j, j = i + temp)
    console.log(j);  // 피보나치 수열

// for (;;) console.log("나는 계속 돌거다~~"); // 무한루프

let s = '3';
for (; s.lengt < 10; s = ' ' + s) ;
for(let x=0.2;x<3.0;x += 0.2)
    console.log(x);

for(;!player.isBroke;)
    console.log("still playing!");


