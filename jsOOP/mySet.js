class mySet {
    constructor(arr) {
        if (!Array.isArray(arr)) {
            throw TypeError('not iterable')
        }
        this.arr = arr
    }

    add(ele) {
        if (!this.has(ele)) {
            this.arr.push(ele)
        }
    }

    has(ele) {
        return this.arr.includes(ele)
    }

    delete(ele) {
        this.arr = this.arr.filter((x) => x !== ele)
    }

    get size() {
        return this.arr.length
    }
}

let s = new mySet(1, 2, 3, 4)

s.delete(3)

console.log(s)

console.log(s.has(4))
console.log(s.has(3))
console.log(s.size)
