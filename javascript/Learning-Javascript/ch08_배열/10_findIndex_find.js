// 일치하는게 없으면 -1 리턴.
// 보조함수를 써서 검색 조건을 지정할 수 있으므로 indexOf보다 더 다양한 상황에서 활용할 수 있다.
// 다만 검색을 시작할 인덱스 지정 불가함.

const arr = [{id: 5, name: "Judith"}, {id: 7, name: "Francis"}];
console.log(arr.findIndex(o => o.id === 5));
console.log(arr.findIndex(object => object.name === "Francis"));
console.log(arr.findIndex(obj => obj === 3));
console.log(arr.findIndex(x => x.id === 17));

// 조건에 맞는 요소의 인덱스가 아니라, '요소자체' 를 원할때.
// 검색조건을 함수로 전달 가능하다.

console.log(arr.find(x => x.id === 5));
console.log(arr.find(x => x.name === 'Francis'));
console.log(arr.find(x => x.id === 10)); // 없으면 undefined.

// find와 findIndex에 전달하는 함수는
// 1. 배열의 각 요소를 첫번째 매개변수로 받고
// 2. 현재 요소의 인덱스와 배열 자체도 매개변수로 받는다.
const numbers = [1, 17, 16, 5, 4, 16, 10, 3, 49];
// 인덱스가 2보다 크고, 제곱수인것
console.log(numbers.find((x, i) => i > 2 && Number.isInteger(Math.sqrt(x))));

// find와 findIndex에 전달하는 함수의 'this' 도 수정할 수 있다.
// 이를 이용해 함수가 객체의 메서드인 것처럼 호출할 수도 있다.

class Person{
    constructor(name){
        this.name = name;
        this.id = Person.nextId++;
    }
}

Person.nextId = 0;
const jamie = new Person("Jamie"),
    juliet = new Person("Juliet"),
    peter = new Person("Peter"),
    jay = new Person("Jay");

const persons = [jamie,juliet,peter,jay];

console.log(persons.find(person => person.id === juliet.id));
console.log(persons.find(function(person){
    return person.id === this.id
},juliet));