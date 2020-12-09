const util = require('./util.js');

function sumUpTo(array, goal) {
	let set = new Set()
	array.forEach(x => set.add(x))
	for (let x of array) {
		if (set.has(goal - x) && 2*x != goal)
			return true
	}
	return false
}

(function() {
	let input = util.readLines('input/day09.txt')
	let numbers = input.map(x => parseInt(x))

	const prevNumberCount = 25
	let lastNumbers = [...numbers.slice(0, prevNumberCount)]
	let firstFail = null
	
	for (let i = prevNumberCount; i < numbers.length; i++) {
		let hasSum = sumUpTo(lastNumbers, numbers[i])
		if (!hasSum) {
			firstFail = numbers[i]
			break
		}
		lastNumbers.shift()
		lastNumbers.push(numbers[i])
	}

	let contigSet = [numbers[0], numbers[1]]
	for (let i = 2; i < numbers.length; i++) {
		let contigSum = contigSet.reduce((a, b) => a + b, 0)
		while (contigSum > firstFail) {
			contigSet.shift()
			contigSum = contigSet.reduce((a, b) => a + b, 0)
		}
		if (contigSum == firstFail)
			break
		contigSet.push(numbers[i])
	}

	let small = Math.min(...contigSet)
	let large = Math.max(...contigSet)

	console.log(firstFail) // 14360655
	console.log(small + large) // 1962331
}())
