// reduce는 배열 자체를 변형한다.
// 보통 배열을 값 하나로 줄이는 데 쓰인다.

// * reduce가 받는 첫번째 매개변수는 배열이 줄어드는 대상인 '어큐뮬레이터' 이다.
// 두 번째 매개변수부터는 동일하게 현재배열요소, 인덱스, 배열 자체이다.

// 초깃값도 옵션 가능.

const arr = [5, 7, 2, 4];
const num = arr.reduce((acc, x) => {
    console.log(acc, x);
    return acc += x;
}, 0);
console.log(num);

// 초깃값 생략시
const num2 = arr.reduce((acc, x) => acc += x);
console.log(num2);

//객체 또한 누적값이 될 수 있다.
const words = ["Beachball", "Rodeo", "Angel", "Aardvark", "Xylophone", "November", "Chocolate", "Papaya", "Uniform", "Joker", "Clover", "Bali"];

const alphabetical = words.reduce((acc, x) => {
    if (!acc[x[0]]) acc[x[0]] = []; // 객체의 키에 첫글자가 없으면 빈배열 추가해주기.
    acc[x[0]].push(x); // 해당 단어 추가.
    return acc;
}, {});
console.log(alphabetical);

//  통계에서도 사용한다.
const data = [3.3, 5, 7.2, 12, 4, 6, 10.3];

const stats = data.reduce((a, x) => {
    a.N++;
    let delta = x - a.mean;
    a.mean += delta / a.N;
    a.M2 += delta * (x - a.mean);
    return a;
}, {N: 0, mean: 0, M2: 0});
console.log(stats);
if (stats.N > 2) {
    stats.variance = stats.M2 / (stats.N - 1);
    stats.stdev = Math.sqrt(stats.variance);
}
console.log(stats);

const longWords = words.reduce((a, word) => word.length > 6 ? a + " " + word : a, "").trim();
console.log(longWords);

const longwds = words.filter(word => word.length > 6).join(' ');
console.log(longwds);
