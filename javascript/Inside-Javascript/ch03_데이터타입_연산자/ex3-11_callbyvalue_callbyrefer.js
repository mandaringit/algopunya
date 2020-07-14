const a = 100;
const objA = {value: 100};


function changeArg(num, obj) {
  num = 200;
  obj.value = 200;

  console.log(num);
  console.log(obj);
}

changeArg(a, objA);

console.log(a);
console.log(objA);
