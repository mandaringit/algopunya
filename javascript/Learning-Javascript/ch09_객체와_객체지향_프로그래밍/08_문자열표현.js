class Car{
    constructor(make,model){
        this.make = make;
        this.model = model;
    }
    toString(){
        return `${this.make} ${this.model}`
    }
}

const c1 = new Car("Tesla","Model S");
console.log(c1.toString());