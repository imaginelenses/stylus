class ExtendedSet extends Set {
    constructor(arr) {
        super(arr)
        this.originalArray = arr
    }

    toArray() {
        return Array.from(this.arr)
    }

    reset() {
        this.arr = this.originalArray
        return this.originalArray
    }

    map(f) {
        let newArray = []
        for(let i in this.arr) {
            newArray.push(f(this.arr[i]))
        }
        return newArray
    }
}


let s = new ExtendedSet([1, 2, 3, 4])
s.delete(4)
s.add(13)
console.log(s)
console.log(s.reset())

console.log(s.toArray())

console.log(s.map((x) => x + 1))

console.log(s.arr)

