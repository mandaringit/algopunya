// 심볼은 유일한 토큰을 나타내기 위해 ES6에서 도입한 새 데이터 타입.
// 심볼은 항상 유일하다
// 다른 어떤 심볼과도 일치하지 않는다. => 이런 면에서 객체와 유사하다.

// 유일하다는 점을 제외하면 원시값의 특성을 모두 가진다.

// 우연히 다른 식별자와 혼동해서는 안되는 고유한 식별자가 필요하다면 심볼을 사용하자.
const RED = Symbol("The color of a sunset!");
const ORANGE = Symbol("The color of a sunset!");
console.log(RED == ORANGE); // false


