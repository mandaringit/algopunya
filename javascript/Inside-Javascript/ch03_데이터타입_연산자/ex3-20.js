const arr = ['zero', 'one', 'two'];
console.log(arr.length);

arr.color = 'blue';
arr.name = 'number_array';
console.log(arr.length);

arr[3] = 'red';
console.log(arr.length);

console.dir(arr);

for (let prop in arr) {
  console.log(prop, arr[prop]);
}

for (let prop in arr) {
  if (arr.hasOwnProperty(prop)) {
    console.log(prop, arr[prop])
  }
}

for (let i = 0; i < arr.length; i++) {
  console.log(i, arr[i])
}


