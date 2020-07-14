// 사용자 객체가 여럿 있고, 이들에게 각각 역할을 부여한다 치자.
const u1 = {name: 'Cynthia'};
const u2 = {name: 'Jackson'};
const u3 = {name: 'Olive'};
const u4 = {name: 'James'};

// 맵생성
const userRoles = new Map();

// 맵의 set() 메서드를 써서 할당.
// userRoles.set(u1,'User');
// userRoles.set(u2,'User');
// userRoles.set(u3,'Admin');

// set() 메서드는 체인으로 연결할 수 있어 수고를 덜 수 있다.
userRoles
  .set(u1, 'User')
  .set(u2, 'User')
  .set(u3, 'Admin');

// 생성자에 배열의 배열을 넘기는 형태로 써도 가능하다.
const userRoles2 = new Map([
  [u1, 'User'],
  [u2, 'User'],
  [u3, 'Admin'],
]);

// 역할을 알아볼때는 (value를 알아볼때)
console.log(userRoles.get(u1));
console.log(userRoles.get(u3));

// 존재하지 않는 키엔 undefined 반환.
console.log(userRoles.get(u4));

// 키가 존재하는지 확인하는 has() 메서드.
console.log(userRoles.has(u1));
console.log(userRoles.has(u4)); // false

// 존재하는 키에 set() 호출시 값이 교체.
console.log(userRoles.get(u1));
userRoles.set(u1,'Admin');
console.log(userRoles.get(u1));

// size 프로퍼티는 맵의 요소 숫자를 반환.
console.log(userRoles.size);

// 이하 "이터러블 객체"이므로 for ... of 루프를 쓸 수 있다.
// .keys() 메서드는 맵의 키를 배열로,
console.log("--- keys() ---");
for (let u of userRoles.keys())
  console.log(u.name);

// values() 메서드는 맵의 값을 배열로,
console.log("--- values() ---");
for (let r of userRoles.values())
  console.log(r);

// entries() 메서드는 첫번째 요소가 키이고 두번째 요소가 값인 배열을 반환
console.log("--- entries() ---");
console.log(userRoles.entries());
for(let ur of userRoles.entries())
  console.log(`${ur[0].name}: ${ur[1]}`);

// 맵도 분해가능.
for (let [u,r] of userRoles.entries())
  console.log(`${u.name}: ${r}`);

// entries() 메서드는 맵의 기본 이터레이터.
// 위 코드를 단축해서 쓸 수 있다.
for (let [u,r] of userRoles)
  console.log(`${u.name}: ${r}`);

// 이터러블 객체보다 배열이 필요하면 확산연산자 사용.
const arrValues = [...userRoles.values()];
console.log(arrValues);

// 맵의 요소를 지울때는 delete() 사용
userRoles.delete(u2);
console.log(userRoles.size);

// 맵의 요소를 모두 지울때는 clear() 사용
userRoles.clear();
console.log(userRoles.size);