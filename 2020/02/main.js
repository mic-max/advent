const util = require('../util.js')

function isValidPassword1(min, max, letter, password) {
	let timesSeen = 0
	for (let char of password) {
		if (char === letter)
			timesSeen++
	}
	return util.inRangeInclusive(timesSeen, min, max)
}

function isValidPassword2(index1, index2, letter, password) {
	return password[index1 - 1] === letter ^ password[index2 - 1] === letter
}

(function() {
	let input = util.readLines('input.txt')

	let totalValidPasswords1 = 0
	let totalValidPasswords2 = 0

	for (let line of input) {
		let match = /^(\d+)-(\d+) ([a-z]): ([a-z]+)$/.exec(line)
		let [a, b, letter, password] = match.slice(1, 5)
		a = parseInt(a)
		b = parseInt(b)

		totalValidPasswords1 += isValidPassword1(a, b, letter, password) ? 1 : 0
		totalValidPasswords2 += isValidPassword2(a, b, letter, password) ? 1 : 0
	}

	console.log(totalValidPasswords1) // 493
	console.log(totalValidPasswords2) // 593
}())
