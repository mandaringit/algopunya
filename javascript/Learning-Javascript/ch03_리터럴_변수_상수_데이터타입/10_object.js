// 객체의 본질은 컨테이너이다.
// 내용물은 바뀔 수 있지만, 컨테이너가 바뀌는건 아니다. 즉, 여전히 같은 객체다.

// 빈 객체
const obj = {}; // 객체의 이름은 의미를 알 수 있게 쓰는걸 권장.

// 객체의 콘텐츠는 프로퍼티(또는 멤버)라고 한다.
// 프로퍼티는 이름(키)와 값으로 구성된다.
// 이름은 반드시 문자열 또는 심볼
// 값은 어떤 타입, 어떤 객체든 상관없다.

// 유효한 식별자를 쓰면 => "접근 연산자(.)"를 사용해도 좋다.
obj.color = 'yellow';

// 유효한 식별자가 아닌 이름을 쓴다면, "계산된 멤버 접근 연산자([])"를 써야한다.
obj["not an identifier"] = 3;
console.log(obj["not an identifier"]);
console.log(obj["color"]);

// 심볼 프로퍼티에 접근할 때도 대괄호를 쓴다.
const SIZE = Symbol();
obj[SIZE] = 8;
console.log("심볼접근 =>", obj[SIZE]);
obj.SIZE = 0;
console.log("SIZE라는 프로퍼티 접근 =>", obj.SIZE);
console.log(obj);

// 말해두지만, 계속해서 바뀌는건 obj 의 프로퍼티들이다.

const sam1 = {
    name: 'Sam',
    age: 4,
};
const sam2 = {name: 'Sam', age: 4};

// 둘의 프로퍼티는 동일하지만, 서로 다른 객체다.
console.log(sam1 == sam2); // false

const sam3 = {
    name: 'Sam',
    classification: {
        kingdom: 'Anamalia',
        phylum: 'Chordata',
        class: 'Mamalia',
        order: 'Carnivoria',
        family: 'Felidae',
        subfamily: 'Felinae',
        genus: 'Felis',
        species: 'catus'
    }
};
// sam3의 family에 접근하는 방법들.
console.log(sam3.classification.family);
console.log(sam3["classification"].family);
console.log(sam3.classification["family"]);
console.log(sam3["classification"]["family"]);

// 함수도 담긴다.
sam3.speak = function () {
    return "Meow!";
};

console.log(sam3.speak()); // 호출 가능

// 객체의 프로퍼티 제거시, delete사용.
delete sam3.classification;
delete sam3.speak;

console.log(sam3)
