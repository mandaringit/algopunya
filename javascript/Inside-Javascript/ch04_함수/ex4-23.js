const myObject = {
  name: 'foo',
  sayName: function () {
    console.log(this.name)
  },
}

const otherObject = {
  name: 'bar',
}

otherObject.sayName = myObject.sayName;

// this는 해당 메서드를 호출한 객체로 바인딩 된다.
myObject.sayName();
otherObject.sayName();