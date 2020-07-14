// 정해진 값으로 배열을 채운다.
// 크기를 지정해 배열을 생성하는 Array 생성자와 잘 어울린다.

const arr = new Array(5).fill(1);
console.log(arr);
arr.fill('a');
console.log(arr);
// 일부만 채울때는 시작과 끝 인덱스를 지정하면 된다.
arr.fill('b',1); // 1번부터 ~
console.log(arr);
arr.fill("c",2,4);
console.log(arr);
// 음수 인덱스도 가능하다.
arr.fill(5.5,-4);
console.log(arr);
arr.fill(0,-3,-1);
console.log(arr);

