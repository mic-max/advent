const util = require('./util.js')

function twoEntriesSummingTo(list, sumGoal) {
	let seenValues = new Set()
	
	for (let value of list) {
		const target = sumGoal - value
		if (seenValues.has(target))
			return value * target
		seenValues.add(value)
	}

	return -1
}

function threeEntriesSummingTo(list, sumGoal) {
	// Gave up on trying to be efficient here :/
	for (let i = 0; i < list.length - 2; i++) {
		for (let j = i + 1; j < list.length - 1; j++) {
			for (let k = j + 1; k < list.length; k++) {
				if (list[i] + list[j] + list[k] === sumGoal)
					return list[i] * list[j] * list[k]
			}
		}
	}
	
	return -1
}

let input = util.readLines('day01_input.txt').map(x => parseInt(x))

let answer1 = twoEntriesSummingTo(input, 2020)
console.log(answer1)

let answer2 = threeEntriesSummingTo(input, 2020)
console.log(answer2)
