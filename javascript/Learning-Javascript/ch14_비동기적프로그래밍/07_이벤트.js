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

const countdown = new Countdown(15,13);

// 이벤트 리슨.
countdown.on('tick', function (i) {
  if (i > 0) console.log(i + '...');
});

countdown.go()
  .then(function () {
    console.log('Go')
  }).catch(function (err) {
  console.error(err.message)
});