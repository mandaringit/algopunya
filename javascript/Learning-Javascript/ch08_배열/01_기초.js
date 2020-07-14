// 본질에서 순서가 있는 데이터집합, 0으로 시작하는 숫자형 인덱스 사용.
// 비균질적 => 모든 요소가 같은 타입일 필요가 없다. 다른 배열이나 객체를 포함해도 괜찮음.
// 배열 리터럴은 대괄호로 만든다. 인덱스 접근도 대괄호.
// length 프로퍼티 존재.
// 배열 길이보다 큰 인덱스르 사용해 요소 할당시, 배열은 자동으로 그 인덱스에 맞게 늘어나며, 빈곳은 undefined.
// 생성자로 만들 수도 있지만 그닥 쓰이지 않는다.

const arr1 = [1, 2, 3];
const arr2 = ['one', 2, 'three'];
const arr3 = [[1, 2, 3], ["one", 2, "three"]];
const arr4 = [
    {name: "fred", type: "object", luckyNumbers: [5, 7, 13]},
    [
        {name: "Susan", type: "object"},
        {name: "Anthony", type: "object"},
    ],
    1,
    function () {
        return "arrays can contain function too";
    },
    "three",
    () => "이것도 가능하다고?",
];
console.log(arr1[0]);
console.log(arr1[2]);
console.log(arr3[1]);
console.log(arr4[1][0]);

console.log(arr1.length);
console.log(arr4.length);
console.log(arr4[1].length);

arr1[4] = 5;
console.log(arr1); // 빈곳은 undefined
console.log(arr1.length);

console.log(arr2[10]); // 인덱스 에러가 안나고 undefined. 그리고 접근만으로 배열의 길이가 늘어나진 않는다.
console.log(arr2);
console.log(arr2.length);

// Array 생성자 (거의 안씀)
const arr5 = new Array();
const arr6 = new Array(1, 2, 3);
const arr7 = new Array(2); // 인자가 숫자하나일땐 길이로 인식하나보다.
const arr8 = new Array("2"); // 이건 아이템으로 인식.
console.log(arr5, arr6, arr7, arr8);



