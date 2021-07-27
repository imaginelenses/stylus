function reduce(arr, fn) {
    let result = arr[0]

    for (let i = 1; i < arr.length; i++) {
        result = fn(result, arr[i])
    }

    return result
}

let arr = [1, 2, 3, 4]

function sum(x, y) {
    return x + y
}

function mul(x, y) {
    return x * y
}

console.log("Sum: ", reduce(arr, sum))

console.log("Multiply: ", reduce(arr, mul))