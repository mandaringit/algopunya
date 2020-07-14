import { rangeGenerator } from './rangeGenerator';

const iterator = rangeGenerator(1, 3 + 1);

while (true) {
  const { value, done } = iterator.next();
  if (done) break;
  console.log(value);
}

for (let value of rangeGenerator(4, 6 + 1)) console.log(value);
