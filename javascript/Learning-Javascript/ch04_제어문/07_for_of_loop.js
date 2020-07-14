function rand(m, n) {
    return m + Math.floor((n - m + 1) * Math.random());
}

function randFace() {
    return ["crown", "anchor", "heart", "spade", "club", "diamond"][rand(0, 5)];
}

// ES6에서 새로 생긴 반복문.
// 컬렉션의 요소에 루프를 실행하는 다른 방법이다.

// for (variable of object)
//     statement

// 배열은 물론, 이터러블 객체에 모두 사용 가능한 범용적 루프다.

const hand = [randFace(),randFace(),randFace()];
for (let face of hand)
    console.log(`You rolled.. ${face}!`);

// 배열에 루프를 실행해야 하지만, 각 요소의 인덱스를 알 필요가 없을 때 알맞다.
const hand2 = [randFace(),randFace(),randFace()];
for (let i = 0; i<hand.length;i++)
    console.log(`Roll ${i+1}: ${hand[i]}`);