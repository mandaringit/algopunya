import INameable from './INameable';

let obj: object = { name: 'Jack' };
// object -> INameable 타입으로.
let name1 = (<INameable>obj).name;
let name2 = (obj as INameable).name;
console.log(name1, name2);
