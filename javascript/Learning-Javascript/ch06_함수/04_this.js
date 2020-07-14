// 함수 바디 안에는 특별한 읽기 전용 값인 this가 존재한다.
// 객체지향 프로그래밍 개념에 밀접한 연관이 있다.

// 일반적으로 this는 객체의 프로퍼티인 함수(메서드)에서 의미가 있다.
// 메서드를 호출하면 this는 호출한 메서드를 소유하는 객체가 된다.

const o = {
    name:'Wallace',
    speak(){return `My name is ${this.name}`}
};
console.log(o.speak()); // o에서 불러서 o.name

// this는 함수를 어떻게 선언했느냐가 아니라
// "어떻게 호출했느냐"에 따라 달라진다는것을 이해하자.

const speak = o.speak;
console.log(speak === o.speak);
console.log(speak()); // 어디에 속한지 몰라 this => undefined

// 메서드라는 용어는 원래 객체지향 프로그래밍의 개념이지만,
// 여기선 객체의 프로퍼티이며, 객체 인스턴스에서 호출할 의도로 만든 함수라는 뜻으로 사용.
// 함수에서 this를 사용하지 않으면 그냥 함수라고 지칭하겠다.

//중첩된 함수에서 this를 사용하려다 보면 굉장히 혼란스러운 경우가 많다.
const o2 = {
    name:'Julie',
    greetBackwards:function () {
        function getReverseName() {
            let nameBackwards = '';
            for (let i=this.name.length-1;i>=0;i--){
                nameBackwards += this.name[i];
            }
            return nameBackwards;
        }
        return `${getReverseName()} si eman ym ,olleH`;
    },
};
// console.log(o2.greetBackwards()); // 에러 발생. this가 o2가 아닌 다른것에 묶인다.

// 문제 해결을 위해 this를 다른 변수에 할당한다.
const o3 = {
    name:'Julie',
    greetBackwards:function () {
        const self = this; // 변수에 할당
        function getReverseName() {
            let nameBackwards = '';
            for (let i=self.name.length-1;i>=0;i--){ // this 대신 할당된 변수를 사용
                nameBackwards += self.name[i];
            }
            return nameBackwards;
        }
        return `${getReverseName()} si eman ym ,olleH`;
    },
};
console.log(o3.greetBackwards());

// 화살표 함수를 써도 이 문제를 해결할 수 있다.
