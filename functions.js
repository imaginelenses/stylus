// function print(func) {
//     console.log(func());
// }

// function greet(name) {
//     return 'Hello, ' + name;

// }

let greet = (name) => {
    return 'Hello, ' + name;
}

let greet = (name) => ('Hello, ' + name)


print(() => (greet("Karthik")))


let print = (func) => {
    console.log(func)
}

document.querySelector('button').addEventListener('click', () => {
    return
})

