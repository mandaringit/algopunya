// indexOf는 찾고자 하는 것과 정확히 일치(===) 하는,
// 첫번째 요소의 "인덱스"를 반환한다.
// lastIndexOf 는 배열의 끝에서부터 검색한다.
// 일부만 검색하려면 시작 인덱스를 지정 가능하다.
// 못찾으면 -1 리턴.

const o = {name: "Jerry"};
const arr = [1, 5, "a", o, true, 5, [1, 2], "9"];

console.log(arr.indexOf(5));
console.log(arr.lastIndexOf(5));
console.log(arr.indexOf("a"));
console.log(arr.lastIndexOf("a"));
console.log(arr.indexOf({name:"Jerry"}));
console.log(arr.indexOf(o));
console.log(arr.indexOf([1,2]));
console.log(arr.indexOf("9"));
console.log(arr.indexOf(9));
console.log(arr.indexOf("a",5));
console.log(arr.indexOf(5,5));
console.log(arr.lastIndexOf(5,4)); // 뒤에서부터 ~
console.log(arr.lastIndexOf(true,3));