const var1 = 1;
const var2 = 2;

function func() {
  const var1 = 10;
  const var2 = 20;
  console.log(var1);
  console.log(var2);
}

func();
console.log(var1);
console.log(var2);