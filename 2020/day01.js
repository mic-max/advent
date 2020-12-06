const util = require('./util.js')

function twoEntriesSummingTo(list, sumGoal) {
	let seenValues = new Set()
	for (let value of list) {
		const target = sumGoal - value
		if (seenValues.has(target))
			return value * target
		seenValues.add(value)
	}
}

function threeEntriesSummingTo(list, sumGoal) {
	for (let i = 0; i < list.length - 2; i++) {
		for (let j = i + 1; j < list.length - 1; j++) {
			for (let k = j + 1; k < list.length; k++) {
				if (list[i] + list[j] + list[k] === sumGoal)
					return list[i] * list[j] * list[k]
			}
		}
	}
}

(function() {
	let input = util.readLines('input/day01.txt').map(x => parseInt(x))

	const goalValue = 2020
	let answer1 = twoEntriesSummingTo(input, goalValue)
	let answer2 = threeEntriesSummingTo(input, goalValue)

	console.log(answer1) // 32064
	console.log(answer2) // 193598720
}())
