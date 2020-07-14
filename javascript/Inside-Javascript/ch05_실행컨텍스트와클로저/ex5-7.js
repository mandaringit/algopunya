function outerFunc() {
  const x = 10;
  const innerFunc = function () {
    console.log(x);
  }
  return innerFunc
}

// outerFunc의 실행 컨텍스트가 생성되었다가
const inner = outerFunc();
// outerFunc의 실행 컨텍스트가 소멸하고
// innerFunc의 실행 컨텍스트가 실행되는데,
// innerFunc의 스코프 체인은 outerFunc 변수 객체를 여전히 참조 가능한가?
inner();