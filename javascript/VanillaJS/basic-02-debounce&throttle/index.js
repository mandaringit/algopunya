// 디바운스 없는 경우
const nodebounceInput = document.querySelector('#nodebounce');
function fakeRequest(name) {
  console.count(`${name} REQUEST`);
}
nodebounceInput.addEventListener('input', () => fakeRequest('일반적인'));

// 디바운스 있는 경우
const debounceInput = document.querySelector('#debounce');
let timer; // setTimeout이 리턴하는 아이디를 저장
function debounce(func, time = 1000) {
  // 1. 만약 이전 타임아웃이 있으면 그걸 종료
  if (timer) {
    clearTimeout(timer);
  }
  // 2. 타이머 설정
  timer = setTimeout(function () {
    func();
  }, time);
}
debounceInput.addEventListener('input', () =>
  debounce(() => fakeRequest('디바운스 된'), 400)
);

// 스로틀링
let timer2;
const throttleInput = document.querySelector('#throttle');
function throttle(func, time = 1000) {
  // 타이머가 없을때
  if (!timer2) {
    timer2 = setTimeout(function () {
      timer2 = null;
      func();
    }, time);
  }
}
throttleInput.addEventListener('input', () =>
  throttle(() => fakeRequest('스로틀 된'))
);
