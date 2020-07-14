// 클래스와 인스턴스 생성
class Car {
    constructor(make, model) {
        this.make = make;
        this.model = model;
        this.userGears = ['P', 'N', 'R', 'D'];
        this.userGear = this.userGears[0]
    }

    shift(gear) {
        if (this.userGears.indexOf(gear) < 0) {
            throw new Error(`Invalid gear: ${gear}`)
        }
        this.userGear = gear;
    }
}

// 인스턴스 생성
const car1 = new Car("Tesla", "Model S");
const car2 = new Car("Mazda", "3i");

// 객체가 클래스의 인스턴스인가 ? => instanceof
console.log(car1 instanceof Car);
console.log(car2 instanceof Car);

car1.shift('D');
car2.shift('R');
console.log(car1.userGear);
console.log(car2.userGear);



