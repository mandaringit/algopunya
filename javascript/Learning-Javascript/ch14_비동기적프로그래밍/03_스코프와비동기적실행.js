function countdown() {
  let i; // i를 밖에서 실행
  console.log("CountDown: ");
  for (i = 5; i >= 0; i--) {
    setTimeout(function () {
      console.log(i === 0 ? "Go" : i)
    }, (5 - i) * 1000);
  }
}

countdown();