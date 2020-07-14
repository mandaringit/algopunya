// 메시지에 타임스탬프를 붙이는 로그 클래스가 필요하다고 생각해보자.
class Log {
  constructor() {
    this.messages = [];
  }

  add(message) {
    this.messages.push({message, timestamp: Date.now()});
  }

  // 1. 단순히 이터레이터를 리턴,
  // [Symbol.iterator]() {
  //   return this.messages.values()
  // }

  // 2. 직접 이터레이터 만들기
  [Symbol.iterator]() {
    let i = 0;
    const messages = this.messages;
    return {
      next() {
        if (i >= messages.length)
          return {value: undefined, done: true};
        return {value: messages[i++], done: false}
      },
    }
  }
}

// 이를 순회하려면.. ?
// 이터레이터 추가후 순회가능.
const log = new Log();
log.add("first day at sea");
log.add("spotted whale");
log.add("spotted another vessel");

for (let msg of log){
  console.log(`${msg.message} @ ${msg.timestamp}`)
}

// 이터레이터는 무한한 데이터에도 사용 가능하다..
// 피보나치 수열은 무한히 계속되고, 프로그램에서는 몇 번째 숫자까지 계산해야할지 알 수 없으므로 이터레이터를 사용하기에 알맞다.

class FibonacciSequence {
  [Symbol.iterator]() {
    let a = 0, b = 1;
    return {
      next() {
        let rval = {value: b, done: false};
        b += a;
        a = rval.value;
        return rval
      },
    }
  }
}

const fib = new FibonacciSequence();
let i = 0;
for (let n of fib) {
  console.log(n);
  if (++i > 9) break;
}// 메시지에 타임스탬프를 붙이는 로그 클래스가 필요하다고 생각해보자.
class Log {
  constructor() {
    this.messages = [];
  }

  add(message) {
    this.messages.push({message, timestamp: Date.now()});
  }

  // 1. 단순히 이터레이터를 리턴,
  // [Symbol.iterator]() {
  //   return this.messages.values()
  // }

  // 2. 직접 이터레이터 만들기
  [Symbol.iterator]() {
    let i = 0;
    const messages = this.messages;
    return {
      next() {
        if (i >= messages.length)
          return {value: undefined, done: true};
        return {value: messages[i++], done: false}
      },
    }
  }
}

// 이를 순회하려면.. ?
// 이터레이터 추가후 순회가능.
const log = new Log();
log.add("first day at sea");
log.add("spotted whale");
log.add("spotted another vessel");

for (let msg of log){
  console.log(`${msg.message} @ ${msg.timestamp}`)
}

// 이터레이터는 무한한 데이터에도 사용 가능하다..
// 피보나치 수열은 무한히 계속되고, 프로그램에서는 몇 번째 숫자까지 계산해야할지 알 수 없으므로 이터레이터를 사용하기에 알맞다.

class FibonacciSequence {
  [Symbol.iterator]() {
    let a = 0, b = 1;
    return {
      next() {
        let rval = {value: b, done: false};
        b += a;
        a = rval.value;
        return rval
      },
    }
  }
}

const fib = new FibonacciSequence();
let i = 0;
for (let n of fib) {
  console.log(n);
  if (++i > 9) break;
}