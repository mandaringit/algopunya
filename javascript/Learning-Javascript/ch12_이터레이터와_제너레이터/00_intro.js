const book = ['Twinkle!','How I wonder ..','Up above..','Like a tea tray..','Twinkle, twinkle..','How I wonder what you..'];

const it = book.values();

console.log(it.next());
console.log(it.next());
console.log(it.next());
console.log(it.next());
console.log(it.next());
console.log(it.next());
console.log(it.next());
console.log(it.next());

// for문 흉내내보기
const it2 = book.values();
let current = it2.next();
while(!current.done){
  console.log(current.value);
  current = it2.next()
}

// 이터레이터는 모두 독립적이다.
const it3 = book.values();
const it4 = book.values();
console.log(it3.next());
console.log(it4.next());

console.log(it4.next());
console.log(it3.next());
