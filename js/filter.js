function filter(arr, fn) {
    const newArray = []
    for(let i = 0; i < arr.length; i++) {
        if (fn(arr[i])) {
            newArray.push(arr[i])
        }
    }

    return newArray
}

let arr = [3, 4, 5, 6, 7]

function lessThanFive(x) {
    return x < 5
}

console.log(filter(arr, lessThanFive))