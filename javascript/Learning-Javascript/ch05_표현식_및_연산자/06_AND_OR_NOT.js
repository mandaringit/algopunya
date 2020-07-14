// AND(&&) OR(||) NOT(!)

// 단축평가
const skipIt = true;
let x = 0;
const result = skipIt || x++; // OR 에서 앞에만 true여도 판단이 끝나므로, 뒤의 x++는 실행되지 않는다.
console.log(result, x);

const doIt = false;
let x2 = 0;
const result2 = doIt && x2++; // AND 에서 앞에만 false여도 판단이 끝남. 뒤의 x2++는 실행되지 않는다.
console.log(result2, x2);

// 불리언 피연산자를 사용하면 논리 연산자는 항상 불리언을 반환한다.
// 피연산자가 불리언이 아니라면 "결과를 결정한 값"이 반환된다.

// 이걸 이용하는 자주 쓰는 패턴
// 옵션이 제공 되면, => suppliedOptions
const suppliedOptions = {name:'Jun'};
const options = suppliedOptions || {name:"Default"};
console.log(options);
// 옵션이 제공되지 않으면 (suppliedOptions == null , undefined) => options는 기본값을 갖게 된다.
const suppliedOptions2 = null;
const options2 = suppliedOptions2 || {name:"Default"};
console.log(options2);


