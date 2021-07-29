class Person {
    constructor(name, birthYear) {
        this.name = name
        this.birthYear = birthYear
    }

    greet() {
        console.log('Hello, ' + this.name)
    }

    goodbye() {
        console.log('Goodbye, ' + this.name)
    }

    get age() {
        let currentYear = new Date().getUTCFullYear()
        return currentYear - this.birthYear
    }

    static hello() {
        console.log('Hello, world!')
    }
}

let p1 = new Person('Alice', 2000)
let p2 = new Person('Bob', 1985)

function isElder(p1, p2) {
    return p1.age > p2.age
}

console.log(isElder(p2, p1))

p1.greet()
p2.greet()
p1.goodbye()
p2.goodbye()

p1.hello()


Person.hello()
// Person.greet()
