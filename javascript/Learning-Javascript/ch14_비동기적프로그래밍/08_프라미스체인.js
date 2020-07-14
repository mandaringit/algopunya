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

function launch() {
  return new Promise(function (resolve, reject) {
    console.log("Lift off!");
    setTimeout(function () {
      resolve("In orbit!");
    }, 2 * 1000)
  })
}

const c = new Countdown(15,)
  .on('tick', i => console.log(i + "..."));

c.go()
  .then(launch) // 완료시 launch 실행,
  .then(msg => console.log(msg)) // launch 완료시 resolve되는 msg 출력
  .catch(err => console.log(err));


