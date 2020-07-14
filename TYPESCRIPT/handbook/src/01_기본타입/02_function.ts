function sum(x: number, y: number): number {
	return x + y;
}

sum(3, 5); // 파라미터로 바로 어떤 타입을 넣을지 알 수 있다!

function sumArray(numbers: number[]): number {
	return numbers.reduce((acc, current) => (acc += current), 0); // 배열의 내장함수 사용시에도 타입유추 굿.
}

const total = sumArray([1, 2, 3, 4, 5]);

function returnNothing(): void {
	console.log('I am just saying hello world');
}
