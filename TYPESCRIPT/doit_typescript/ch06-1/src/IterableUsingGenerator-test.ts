import { IterableUsingGenerator } from './IterableUsingGenerator';

for (let item of new IterableUsingGenerator([1, 2, 3])) console.log(item);

for (let item of new IterableUsingGenerator(['hello', 'world', '!']))
  console.log(item);

const iter = new IterableUsingGenerator([1, 2, 3, 4, 5, 67]);
