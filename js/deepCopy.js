let person = {
    name: "Foo",
    address: {
        street: 1
    }
}

function deepCopy (obj) {
    const keys = Object.keys(obj);
    const newObj = {};

    for (let i = 0; i < keys.length; i++) {
        const key = keys[i];
        if (typeof(obj[key]) === 'object') {
            newObj[key] = deepCopy(obj[key])
        }
        else {
            newObj[key] = obj[key]
        }
    }

    return newObj
}

let newPerson = deepCopy(person);

newPerson.name = 'Bar';
newPerson.address.street = 2;

console.log(person, newPerson);