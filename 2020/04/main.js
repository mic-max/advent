const util = require('../util.js')

function validBirthYear(x) { return !isNaN(x) && util.inRangeInclusive(x, 1920, 2002) }
function validIssueYear(x) { return !isNaN(x) && util.inRangeInclusive(x, 2010, 2020) }
function validHairColour(x) { return /^#[\da-f]{6}$/.test(x) }
function validEyeColour(x) { return ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'].includes(x) }
function validPassportId(x) { return /^\d{9}$/.test(x) }
function validExpirationYear(x) { return !isNaN(x) && util.inRangeInclusive(x, 2020, 2030) }
function validHeight(x) {
	let match = /^(\d+)(cm|in)$/.exec(x)
	if (match === null)
		return false

	let [min, max] = match[2] === 'cm' ? [150, 193] : [59, 76]
	return util.inRangeInclusive(parseInt(match[1]), min, max)
}

function addFieldsToPassport(passport, fieldLine) {
	for (let field of fieldLine.split(' ')) {
		let parts = field.split(':')
		passport[parts[0]] = parts[1]
	}
}

function isValidPassport(passport) {
	return ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'].every(x => passport.hasOwnProperty(x))
}

function isStrictlyValidPassport(passport) {
	return validBirthYear(passport.byr)
		&& validIssueYear(passport.iyr)
		&& validExpirationYear(passport.eyr)
		&& validHeight(passport.hgt)
		&& validHairColour(passport.hcl)
		&& validEyeColour(passport.ecl)
		&& validPassportId(passport.pid)
}

(function() {
	let input = util.readLines('input.txt')

	let passport = {}
	let validPassportCount = 0
	let strictlyValidPassportCount = 0

	for (let line of input) {
		if (line === '') {
			if (isValidPassport(passport)) {
				validPassportCount++
				strictlyValidPassportCount += isStrictlyValidPassport(passport) ? 1 : 0
			}
			passport = {}
			continue
		}
		
		addFieldsToPassport(passport, line)
	}
	
	console.log(validPassportCount) // 242
	console.log(strictlyValidPassportCount) // 186
}())
