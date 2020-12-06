const util = require('./util.js')

let input = util.readLines('input/day06.txt')

function anySaidYesTo(input) {
	let sumOfYeses = 0
	let currentAnswers = new Set()
	for (let line of input) {
		if (line === '') {
			sumOfYeses += currentAnswers.size
			currentAnswers.clear()
		} else {
			// Add each letter to the set
			line.split('').forEach(x => currentAnswers.add(x))
		}
	}
	return sumOfYeses
}

function allSaidYesTo(input) {
	let passengers = []
	let count = 0
	for (let line of input) {
		if (line === '') {
			let start = passengers[0]
			for (let i = 1; i < passengers.length; i++)
				start = start.filter(x => passengers[i].includes(x))
			count += start.length
			passengers = []
		} else {
			// Add each letter to the set
			passengers.push(line.split(''))
		}
	}

	return count
}

console.log(anySaidYesTo(input))
console.log(allSaidYesTo(input))
