class Car {
}

class InsurancePolicy {
}

function makeInsurable(o) {
  o.addInsurancePolicy = function (p) {
    this.insurancePolicy = p;
  }
  o.getInsurancePolicy = function () {
    return this.insurancePolicy
  }
  o.isInsured = function () {
    return !!this.insurancePolicy
  }
}

// 프로토타입에 다 박아버림
makeInsurable(Car.prototype);
const car1 = new Car(); // 각 인스턴스들이 이제 보험에 가입하는 기능이 추가된다.
car1.addInsurancePolicy(new InsurancePolicy());
console.log(car1.isInsured());

const ADD_POLICY = Symbol();
const GET_POLICY = Symbol();
const IS_INSURED = Symbol();
const _POLICY = Symbol();

function makeInsurable2(o) {
  o[ADD_POLICY] = function (p) {
    this[_POLICY] = p;
  };
  o[GET_POLICY] = function () {
    return this[_POLICY];
  };
  o[IS_INSURED] = function () {
    return !!this[_POLICY];
  };
}
