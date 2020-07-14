// splice - 임의의 위치에 요소 추가하거나 제거하기. (수정) 및 수정된 부분 리턴함.
const arr4 = [1, 5, 7];
let r1 = arr4.splice(1, 0, 2, 3, 4); // 지우지 않고 위치에 추가.
console.log(r1, arr4);
let r2 = arr4.splice(5, 0, 6); // 지우지 않고 위치에 추가.
console.log(r2, arr4);
let r3 = arr4.splice(1, 2); // 1 ~ 2 인덱스 삭제.
console.log(r3, arr4);
let r4 = arr4.splice(2, 1, 'a', 'b'); // 2번째 인덱스 하나 지우고 두개 추가
console.log(r4,arr4);