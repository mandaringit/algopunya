// apply는 함수 매개변수를 처리하는 방법을 제외하면 call과 완전히 같다.
// apply는 매개변수를 배열로 받는다.
const bruce = {name: 'Bruce'};
const madeline = {name: "Madeline"};

function update(birthYear, occupation) {
    this.birthYear = birthYear;
    this.occupation = occupation;
}

update.apply(bruce, [1955, 'actor']);
console.log(bruce);
update.apply(madeline, [1918, 'writer']);
console.log(madeline);

// 배열 요소를 매개변수로 활용할때 유용하다.
// 배열의 최솟값과 최댓값 구하기 예제
arr = [2, 3, -5, 15, 7];
console.log(Math.min.apply(null, arr)); // this와 관계없이 동작하므로 null을 넣어줬다.
console.log(Math.max.apply(null, arr));

// 확산연산자를 사용해도 동일한 효과를 낸다.
const newBruce = [1940, "martial artist"];
update.call(bruce, ...newBruce);
console.log(bruce);
console.log(Math.min(...arr));
console.log(Math.max(...arr));


// bind
// bind를 사용하면 함수의 this 값을 영구히 바꿀 수 있다.
// update 메서드를 이리저리 옮기면서 호출할 때도, this 값은 항상 bruce가 되게끔,
// call 이나 apply, 다른 bind와 함께 호출하더라도 this 값이 bruce가 되도록.

const updateBruce = update.bind(bruce); // 객체를 각인시킨 새로운 함수
updateBruce(1904, "actor");
console.log(bruce);
updateBruce.call(madeline, 1274, "king"); // 객체를 넣어도 바뀌는 객체는 madeline이 아닌 고정된 bruce객체다.
console.log(bruce); // 변화 O
console.log(madeline); // 변화 X

// bind는 함수의 동작을 영구적으로 변경하므로 버그의 원인이 될 수도 있다.
// 유용하지만, 주의해서 사용하도록 하자.

const updateBruce1949 = update.bind(bruce, 1949); // 객체와 태어난 해 까지 고정한 새로운 함
updateBruce1949("singer,songwriter"); // 직업만 바꿀 수 있는 함수가 되었다.
console.log(bruce);