function solution(X, Y) {
  numbers = [];
  ans = [0, 0, 0];
  for (let i = 1; i <= X; i++) {
    numberStr = i.toString();
    if (numberStr.includes(Y.toString())) {
      numbers.push(i);
    }
  }
  if (numbers.length > 0){
    ans[0] = numbers.length;
    ans[1] = numbers.reduce((prev, curr) => prev + curr, 0);
    ans[2] = numbers.reduce((prev, curr) => prev * curr, 1);
  }

  return ans;
}


console.log(solution(5, 6))