const person = {
  name: 'zzoon',
  getName: function () {
    return this.name;
  },
  setName: function (arg) {
    this.name = arg;
  },
}

function create_object(o) {
  function F() {
  }

  F.prototype = o;
  return new F();
}

function extend(obj, prop) {
  if (!prop) {
    prop = obj;
    obj = this;
  }
  for (let i in prop) obj[i] = prop[i];
  return obj;
}

const student = create_object(person);
const added = {
  setAge: function (age) {
    this.age = age;
  },
  getAge: function () {
    return this.age;
  },
};

extend(student, added);

student.setAge(25);
console.log(student.getAge());