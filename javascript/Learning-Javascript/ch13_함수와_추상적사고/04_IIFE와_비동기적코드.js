// 5초에서 시작하고 카운트다운이 끝나면 'go' 표시하는 고전적 타이머 예제

// let 대신 var를 쓴 이유는 IIFE가 중요하던 시점으로 돌아가서
// 왜 중요했는지 이해하기 위함.
// var i;
// for (i = 5; i >= 0; i--) {
//   setTimeout(function () {
//     console.log(i === 0 ? "go" : i);
//   }, (5 - i) * 1000)
// }

// function loopBody(i) {
//   setTimeout(function () {
//     console.log(i === 0 ? 'go' : i);
//   }, (5 - i) * 1000)
// }


for (let i = 5; i >= 0; i--) {
  setTimeout(function () {
    console.log(i === 0 ? 'go' : i);
  }, (5 - i) * 1000)
}