const myObject = {
  name: 'foo',
  sayName: function () {
    console.log('My name is ' + this.name)
  },
}

myObject.sayName();
console.log(myObject.hasOwnProperty('name'));
console.log(myObject.hasOwnProperty('nickname'));
myObject.sayNickName();