// map은 배열 요소를 변형한다. 무엇이든 가능하다.
// 일정한 형식의 배열을 다른 형식으로 바꿔야 한다면 map을 쓰자.
// map과 filter는 모두 사본을 반환하며 원래 배열은 바뀌지 않는다.

const cart = [{name: 'Widget', price: 9.95}, {name: "Gadget", price: 22.95}];
const names = cart.map(product => product.name);
console.log(names);
const prices = cart.map(product => product.price);
console.log(prices);
const discountPrices = cart.map(product => product.price * 0.8);
console.log(discountPrices);

// 콜백 함수는 각 요소에서 호출될 때 요소 자체와 요소 인덱스, 배열 전체를 매개변수로 받는다.
// 인덱스를 이용해 위 둘을 합쳐 객체를 만들었다.
const items = ["Widget", "Gadget"];
const prices2 = [9.95, 22.95];
// 객체를 괄호로 감싼건, 이렇게 안하면 화살표 표기법이 객체 리터럴의 중괄호를 블록으로 판단하기 때문
const cart2 = items.map((name, i) => ({name, price: prices2[i]}));
console.log(cart2);



