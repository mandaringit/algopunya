class Car {
    constructor(make, model) {
        this.make = make;
        this.model = model;
        this._userGears = ['P', 'N', 'R', 'D'];
        this._userGear = this._userGears[0]
    }

    get userGear() {
        return this._userGear;
    }

    set userGear(value) {
        if (this.userGears.indexOf(value) < 0) {
            throw new Error(`Invalid gear: ${value}`)
        }
        this._userGear = value;
    }

    shift(gear) {
        this._userGear = gear;
    }
}

// 아직도 car1_userGear = 'X' 처럼 직접 바꿀순있지만, 적어도 바꾸지 마라는 방편으로 생각.
// 꼭 보호하려면 스코프를 이용해 보호하는 WeakMap 인스턴스를 사용 가능하다.

const Car = (function () {
    const carProps = new WeakMap();

    class Car {
        constructor(make, model) {
            this.make = make;
            this.model = model;
            this._userGears = ['P', 'N', 'R', 'D'];
            carProps.set(this, {userGear: this._userGears[0]});
        }

        get userGear() {
            return carProps.get(this).userGear;
        }

        set userGear(value) {
            if (this._userGears.indexOf(value) < 0) {
                throw new Error(`Invalid gear: ${value}`)
            }
            carProps.get(this).userGear = value;
        }

        shift(gear) {
            this.userGear = gear
        };
    }
});



