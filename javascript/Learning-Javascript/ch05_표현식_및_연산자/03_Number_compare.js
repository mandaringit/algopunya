// NaN에 대해 알아둘것.

// 자신 포함 무엇과도 같지 않다.
console.log(NaN == NaN);
console.log(NaN == NaN);

// 자바스크립트 숫자는 모두 더블형이다.
// 그리고 더블 형식은 근사치이므로, 숫자를 비교하다 곤란한 상황이 자주 보인다.

// 자바스크립트 정수 비교
eps = Number.EPSILON;// 매우 작은 값으로, 숫자 두개를 구별하는 기준으로 사용한다.

let n = 0;
// while(true){
//     n += 0.1;
//     if (n===0.3) break;  // 의외로 빗겨나감. 무한루프가 생긴다.
// }

while (true){
    n += 0.1;
    console.log(n);
    if (Math.abs(n-0.3)<Number.EPSILON) break; // 느슨한 비교를 통해 가능하다.
}



