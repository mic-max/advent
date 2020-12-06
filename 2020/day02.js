const util = require('./util.js')

let input = util.readLines('input/day02.txt')

function isValidPassword1(min, max, letter, password) {
	let timesSeen = 0
	for (let char of password) {
		if (char === letter) {
			timesSeen++
		}
	}

	return min <= timesSeen && timesSeen <= max
}

function isValidPassword2(index1, index2, letter, password) {
	return password[index1 - 1] === letter ^ password[index2 - 1] === letter
}

let totalValidPasswords1 = 0
let totalValidPasswords2 = 0

for (let line of input) {
	let a = parseInt(line.substring(0, line.indexOf('-')))
	let b = parseInt(line.substring(line.indexOf('-') + 1, line.indexOf(' ')))
	let letter = line[line.indexOf(' ') + 1]
	let password = line.substring(line.indexOf(':') + 2)

	if (isValidPassword1(a, b, letter, password))
		totalValidPasswords1++

	if (isValidPassword2(a, b, letter, password))
		totalValidPasswords2++
}

console.log(totalValidPasswords1)
console.log(totalValidPasswords2)
