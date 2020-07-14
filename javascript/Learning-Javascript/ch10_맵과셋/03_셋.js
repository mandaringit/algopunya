// 한 사용자에게 여러 역할을 할당하고 싶다고 하자.
// User는 모두에게 할당 되지만, 관리자는 "Admin"역할을 동시에 가질 수 있다.

// Set 인스턴스 생성
const roles = new Set();
roles.add("User");
console.log(roles);
roles.add("Admin");
console.log(roles);

// size 프로퍼티 리턴.
console.log(roles.size);

roles.add("User"); // 같은건 또 들어가지 않는다.
console.log(roles.size); // 사이즈

// 제거시엔 delete()
roles.delete("Admin");
console.log(roles);
console.log(roles.delete("Admin")); // 없으면 false


