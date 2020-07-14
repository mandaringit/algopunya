// concat - 배열 끝에 여러 요소를 추가한 '사본 반환'
const arr2 = [1, 2, 3];
let a1 = arr2.concat(4, 5, 6);
console.log(a1, arr2);
let a2 = arr2.concat([4, 5, 6]); // 배열 삽입시, 분해해서 추가함.
console.log(a2, arr2);
let a3 = arr2.concat([4, 5], 6);
console.log(a3, arr2);
let a4 = arr2.concat([4, [5, 6]]); // *분해는 한번만한다.
console.log(a4, arr2);