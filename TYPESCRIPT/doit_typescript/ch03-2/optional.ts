interface IPerson {
  name: string;
  age: number;
  etc?: boolean;
}

let good1: IPerson = {
  name: 'Jack',
  age: 32,
};

let good2: IPerson = {
  name: 'Jack',
  age: 32,
  etc: true,
};
