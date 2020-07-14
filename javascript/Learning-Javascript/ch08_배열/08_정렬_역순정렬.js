const arr = [1, 2, 3, 4, 5];

// reverse => 요소 순서 변경.
arr.reverse();
console.log(arr);

// 정렬.
arr.sort();
console.log(arr);

// sort는 *정렬 함수를 받을 수 있다.
const arr2 = [
	{ name: 'Suzanne' },
	{ name: 'Jim' },
	{ name: 'Trevor' },
	{ name: 'Amanda' },
];
console.log(arr2); // 정렬되는게 없다
arr2.sort((a, b) => a.name > b.name); // 알파벳 순.
console.log(arr2);
arr2.sort((a, b) => a.name[1] < b.name[1]); // 알파벳 두번째 글자. 알파벳 역순.
console.log(arr2);
