// Functional Inheritance (Prototype-based)
    function Car(make, model, year) {
      this.make = make;
      this.model = model;
      this.year = year;
    }

    Car.prototype.getMake = function () {
      return this.make;
    };

    Car.prototype.getModel = function () {
      return this.model;
    };

    Car.prototype.getYear = function () {
      return this.year;
    };

    Car.prototype.getCarInfo = function () {
      return `Make: ${this.make}, Model: ${this.model}, Year: ${this.year}`;
    };

    function Sedan(make, model, year, color) {
      Car.call(this, make, model, year);
      this.color = color;
    }

    Sedan.prototype = Object.create(Car.prototype);

    Sedan.prototype.getColor = function () {
      return this.color;
    };

    Sedan.prototype.getCarInfo = function () {
      return `Make: ${this.make}, Model: ${this.model}, Year: ${this.year}`;
    };

    const car = new Car("Toyota", "Corolla", 2022);
    document.getElementById("makePrototype").innerText = car.getMake();
    document.getElementById("modelPrototype").innerText = car.getModel();
    document.getElementById("yearPrototype").innerText = car.getYear();
    document.getElementById("carPrototypeInfo").innerText = car.getCarInfo();

    const sedan = new Sedan("Honda", "Accord", 2020, "Red");
    document.getElementById("colorSedan").innerText = sedan.getColor();
    document.getElementById("sedanPrototypeInfo").innerText = sedan.getCarInfo();

    // Class and Extends
    class CarClass {
      constructor(make, model, year) {
        this.make = make;
        this.model = model;
        this.year = year;
      }

      getMake() {
        return this.make;
      }

      getModel() {
        return this.model;
      }

      getYear() {
        return this.year;
      }

      getCarInfo() {
        return `Make: ${this.make}, Model: ${this.model}, Year: ${this.year}`;
      }
    }

    class SedanClass extends CarClass {
      constructor(make, model, year, color) {
        super(make, model, year);
        this.color = color;
      }

      getColor() {
        return this.color;
      }

      getCarInfo() {
        return `Make: ${this.make}, Model: ${this.model}, Year: ${this.year}`;
      }
    }

    const carClass = new CarClass("Toyota", "Corolla", 2022);
    document.getElementById("makeClass").innerText = carClass.getMake();
    document.getElementById("modelClass").innerText = carClass.getModel();
    document.getElementById("yearClass").innerText = carClass.getYear();
    document.getElementById("carClassInfo").innerText = carClass.getCarInfo();

    const sedanClass = new SedanClass("Honda", "Accord", 2020, "Blue");
    document.getElementById("colorClassSedan").innerText = sedanClass.getColor();
    document.getElementById("sedanClassInfo").innerText = sedanClass.getCarInfo();