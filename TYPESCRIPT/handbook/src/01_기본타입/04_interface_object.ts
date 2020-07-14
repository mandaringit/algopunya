interface Person {
	name: string;
	age?: number; // 있어도 되고 없어도 되고
}

interface Developer extends Person {
	skills: string[];
}

const person: Person = {
	name: '김사람',
	age: 20,
};

const expert: Developer = {
	name: '김개발',
	skills: ['javascript', 'typescript'],
};

const people: Person[] = [person, expert];
