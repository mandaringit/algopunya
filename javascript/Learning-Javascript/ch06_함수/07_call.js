// call method
const bruce = {name: 'Bruce'};
const madeline = {name: "Madeline"};

function greet() {  // 어떤 객체에도 묶이지 않았지만 this를 쓴다.
    return `Hello,I'm ${this.name}!`;
}

console.log(greet()); // this는 어디에도 묶이지 않는다.
console.log(greet.call(bruce)); // this는 bruce이다.
console.log(greet.call(madeline)); // this는 madeline이다.

//함수를 호출하면서 call을 사용하고 "this로 사용할 객체를 넘기면" 해당 함수가 주어진 객체의 메서드인 것처럼 사용 가능.
function update(birthYear, occupation) {
    this.birthYear = birthYear;
    this.occupation = occupation;
}
// call(this로 사용할 객체, 나머지 매개변수)
update.call(bruce, 1949, 'singer');
console.log(bruce);
update.call(madeline, 1942, 'actress');
console.log(madeline);

