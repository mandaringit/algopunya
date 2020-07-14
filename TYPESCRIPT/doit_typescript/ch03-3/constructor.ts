class Person2 {
  constructor(public name: string, public age?: number) {}
}

let jack2: Person2 = new Person2('Jack', 32);
console.log(jack2);

// 위는 아래를 함축해서 구현한 것이라고 볼 수 있다.

class Person3 {
  name: string;
  age?: number;
  constructor(name: string, age?: number) {
    this.name = name;
    this.age = age;
  }
}

let jack3: Person3 = new Person3('Jack', 32);
console.log(jack3);
