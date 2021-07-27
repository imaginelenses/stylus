const person1 = {
    name: 'Vidhya',
    greet: function() { console.log('Hello, ' + this.name) }
}

console.dir(person1)
person1.greet()

const person2 = {
    name: 'Omkar'
}

person2.greet = person1.greet

console.dir(person2)
person2.greet()