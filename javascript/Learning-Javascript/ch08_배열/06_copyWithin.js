// 배열 요소를 복사해서 다른 위치에 붙여넣고, 기존 요소를 덮어 쓴다.
const arr = [1,2,3,4];
// target => 복사요소 붙여넣을 위치 , start => 복사 시작 위치 , end => 복사 끝 위치(생략시 끝까지)
// 음수 인덱스를 사용하면 배열의 끝에서부터 센다.
arr.copyWithin(1,2);
console.log(arr);
arr.copyWithin(2,0,2); // 0 ~ 1까지 복사해서, 2번째 인덱스부터 덮어쓰기.
console.log(arr);
arr.copyWithin(0, -3,-1); // -3 ~ -2 까지 복사해서, 0번째 인덱스부터 덮어쓰기
console.log(arr);


