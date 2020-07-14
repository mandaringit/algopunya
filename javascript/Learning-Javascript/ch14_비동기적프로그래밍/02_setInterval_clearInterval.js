const start = new Date();
let i = 0;
const intervalId = setInterval(function () {
  let now = new Date();
  if (now.getMinutes() !== start.getMinutes() || ++i > 10) {
    console.log('종료합니다.');
    return clearInterval(intervalId);
  }
  console.log(`${i}:${now}`);
}, 5 * 1000);
