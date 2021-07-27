function map(arr, fn) {
    const newArray = []
    for(let i = 0; i < arr.length; i++) {
        newArray.push(fn(arr[i]))
    }

    return newArray
}

let arr = [0, 1, 2, 3, 4]

let result = map(arr, (x) => {
    return x * x
})

console.log("result: ", result)

function lessThanFive(x) {
    return x < 5
}

console.log("filter: ", result.filter(lessThanFive))

function sum(x, y) {
    return x + y
}

console.log("reduce: ", result.reduce(sum))

