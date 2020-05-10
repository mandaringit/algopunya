process.stdin.setEncoding('utf8');
process.stdin.on('data', data => {
  console.log(data)
  const n = data.split(" ");
  const a = Number(n[0]), b = Number(n[1]);
  console.log(a);
  console.log(b);
});

function solution(v) {
  var answer = [
    []
  ];

  console.log('Hello Javascript')

  return answer;
}