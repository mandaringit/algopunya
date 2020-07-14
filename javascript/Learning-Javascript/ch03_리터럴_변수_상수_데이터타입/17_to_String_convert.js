// 자바스크립트 "모든객체" 에는 문자열 표현을 반환하는 toString() 메서드가 있다.
// 그다지 쓸일은 많지 않다. 병합에서 자동으로 숫자를 문자열로 변환하기 때문에.

// 숫자에서 문자열로.. 쓸만한 결과를 반환.
const n = 33.5;
console.log(typeof n,n);

const s = n.toString();
console.log(typeof s,s);

// Date 객체를 문자열로.. 그럭저럭 쓸만함.
const now = new Date();
const now_s = now.toString();
console.log(typeof now_s,now_s);

// 배열의 toString()은 꽤 쓸모있다.
const arr = [1,true,"hello"];
console.log(typeof arr.toString(),arr.toString());  // 각 요소를 문자열로 바꾸고, 쉼표로 연결한 결과를 반환.

// 대부분은 [object Object]같은 별 쓸모도 없는걸 반환한다.


