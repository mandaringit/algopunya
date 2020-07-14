function* rainbow() {
    yield 'red';
    yield 'orange';
    yield 'yellow';
    yield 'green';
    yield 'blue';
    yield 'indigo';
    yield 'violet';
}

// 제너레이터 호출 시 이터레이터를 얻는다.

const it = rainbow();
console.log(it.next());
console.log(it.next());
console.log(it.next());
console.log(it.next());
console.log(it.next());
console.log(it.next());
console.log(it.next());
console.log(it.next());

for (let color of rainbow()){
    console.log(color);
}

function* interrogate(){
    const name = yield "What is your name?";
    const color = yield "What is your favorite color?";
    return `${name}'s favorite color is ${color}`;
}

const iter = interrogate();
console.log(iter.next());
console.log(iter.next('Ethan'));
console.log(iter.next('orange'));

function* abc(){
    yield 'a';
    yield 'b';
    return 'c';
}

const alpha = abc();
console.log(alpha.next());
console.log(alpha.next());
console.log(alpha.next());

for (let al of abc()){
    console.log(al)
}