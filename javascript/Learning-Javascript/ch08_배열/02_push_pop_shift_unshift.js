// 일부는 배열 '자체'를 수정하고
// 일부는 새 배열을 리턴한다.
// 이걸 모두 기억해야 한다;;

// push - 뒤에서 추가 ,pop - 뒤에서 제거. 스택에 해당하는 행동. (수정됨)
const arr = ["b", "c", "d"];
l = arr.push("e", "f"); // 끝에서 증가, 늘어난 길이 반환.
console.log(l, arr);
el = arr.pop(); // 끝에서 뽑은 요소 반환.
console.log(el, arr);

// shift - 앞에서 제거, unshift - 앞에서 증가.  큐에 해당하는 행동. (수정됨)
el2 = arr.shift();
console.log(el2, arr);
l2 = arr.unshift("a");
console.log(l2, arr);





