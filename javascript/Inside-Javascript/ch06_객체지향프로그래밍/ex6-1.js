function Person(arg) {
  this.name = arg;

  this.getName = function () {
    return this.name;
  }

  this.setName = function (value) {
    this.name = value;
  }
}

const me = new Person('zzoon');
console.log(me.getName());

me.setName('iamhjoo');
console.log(me.getName())

const you = new Person('you');
const him = new Person('him');