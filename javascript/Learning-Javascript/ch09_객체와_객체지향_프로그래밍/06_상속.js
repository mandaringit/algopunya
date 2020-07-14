class Vehicle{
    constructor(){
        this.passengers = [];
        console.log("Vehicle created");
    }
    addPassenger(p){
        this.passengers.push(p)
    }
}

class Car extends Vehicle{
    constructor(){
        super();
        console.log("Car Created");
    }
    deployAirbags(){
        console.log("Bwoosh!");
    }
}

const v = new Vehicle();
v.addPassenger("Frank");
v.addPassenger("Judy");
console.log(v.passengers);

const c = new Car();
c.addPassenger("Alice");
c.addPassenger("Cameron");
console.log(c.passengers);

// v.deployAirbags(); // error
c.deployAirbags();

class MotorCycle extends Vehicle{}
const m = new MotorCycle();
console.log(c instanceof Car);
console.log(c instanceof Vehicle);
console.log(m instanceof Car);
console.log(m instanceof MotorCycle);
console.log(m instanceof Vehicle);