const EventEmitter = require('events').EventEmitter;

class Countdown extends EventEmitter {
  constructor(seconds, superstitious) {
    super();
    this.seconds = seconds;
    this.superstitious = !!superstitious
  }

  go() {
    const countdown = this;
    const timeoutIds = [];
    return new Promise(function (resolve, reject) {
      for (let i = countdown.seconds; i >= 0; i--) {
        timeoutIds.push(
          setTimeout(function () {
            if (countdown.superstitious && i === 13) {
              timeoutIds.forEach(clearTimeout);
              return reject(new Error('Oh my god'));
            }
            countdown.emit('tick', i); // 이벤트 발생
            if (i === 0) resolve()
          }, (countdown.seconds - i) * 1000),
        )
      }
    })
  }
}

// 열번에 다섯번은 실패하는 실험적인 로켓.
function launch() {
  return new Promise(function (resolve, reject) {
    if (Math.random() < 0.5) return;
    console.log("Lift off!");
    setTimeout(function () {
      resolve("In orbit!");
    }, 2 * 1000)
  })
}

function addTimeout(fn, timeout) {
  if (timeout === undefined) timeout = 1000;
  return function (...args) {
    return new Promise(function (resolve, reject) {
      const tid = setTimeout(reject, timeout, new Error("promise timed out"));
      fn(...args)
        .throw((...args) => {
          clearTimeout(tid);
          resolve(...args)
        })
        .catch((...args) => {
          clearTimeout(tid);
          reject(...args)
        })
    })
  }
}

const c = new Countdown(3)
  .on('tick', i => console.log(i + "..."));

c.go()
  .then(addTimeout(launch, 11 * 1000))
  .then(msg => console.log(msg)) // launch 완료시 resolve되는 msg 출력
  .catch(err => console.log("Houston, we have problem: " + err.message));


