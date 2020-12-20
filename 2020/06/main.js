const util = require('../util.js')

function anySaidYesTo(group) {
	let currentAnswers = new Set()
	for (let passenger of group)
		passenger.forEach(x => currentAnswers.add(x))
	return currentAnswers.size
}

function allSaidYesTo(group) {
	let start = group[0]
	for (let i = 1; i < group.length; i++)
		start = start.filter(x => group[i].includes(x))
	return start.length
}

(function() {
	let input = util.readLines('input.txt')

	let group = []
	let anySaidYes = 0
	let allSaidYes = 0
	for (let line of input) {
		if (line === '') {
			anySaidYes += anySaidYesTo(group)
			allSaidYes += allSaidYesTo(group)
			group = []
		} else {
			group.push(line.split(''))
		}
	}

	console.log(anySaidYes) // 6532
	console.log(allSaidYes) // 3427
}())
