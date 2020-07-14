// class는 단축문법일 뿐이며 자바스크립트 클래스 자체가 바뀐것은 아니다.
// 그러니까 자바스크립트 클래스 자체를 이해하는게 더 중요하다.

// ES5 클래스 정의
function Car(make,model){
    this.make = make;
    this.model = model;
    this._userGears = ['P','N','R','D'];
    this._userGear = this._userGears[0];
}

// 결과는 동일하다.
class Es6Car {}
function Es5Car(){}
console.log(typeof Es6Car);
console.log(typeof Es5Car);

// 클래스가 바뀐것은 아니다. 단지 간편한 새 문법이 생겼을 뿐이다.




