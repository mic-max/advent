const util = require('./util.js')

let input = util.readLines('day04_input.txt')

const fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

function isValidPassport(passport) {
	return fields.every(x => passport.hasOwnProperty(x))
}

let validBirthYear = (byr) => !isNaN(byr) && util.inRangeInclusive(byr, 1920, 2002)
let validIssueYear = (iyr) => !isNaN(iyr) && util.inRangeInclusive(iyr, 2010, 2020)
let validExpirationYear = (eyr) => !isNaN(eyr) && util.inRangeInclusive(eyr, 2020, 2030)
let validHeight = (hgt) => {
	let re = /^(\d+)(cm|in)$/
	let match = re.exec(hgt)
	if (match === null)
		return false

	let value = parseInt(match[1])

	if (match[2] === 'cm')
		return util.inRangeInclusive(value, 150, 193)
	return util.inRangeInclusive(value, 59, 76)
}
let validHairColour = (hcl) => /^#[\da-f]{6}$/.test(hcl)
let validEyeColour = (ecl) => ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'].includes(ecl)
let validPassportId = (pid) => /^\d{9}$/.test(pid)

// Requirement: passport argument must pass isValidPassport function
function isStrictlyValidPassport(passport) {
	return validBirthYear(passport.byr)
		&& validIssueYear(passport.iyr)
		&& validExpirationYear(passport.eyr)
		&& validHeight(passport.hgt)
		&& validHairColour(passport.hcl)
		&& validEyeColour(passport.ecl)
		&& validPassportId(passport.pid)
}

function addFieldsToPassport(passport, fieldLine) {
	let passFields = fieldLine.split(' ')
	for (let field of passFields) {
		let parts = field.split(':')
		passport[parts[0]] = parts[1]
	}
}

let passport = {}

let validPassportCount = 0
let strictlyValidPassportCount = 0
for (let i = 0; i < input.length; i++) {
	let line = input[i]
	if (line === '') {
		if (isValidPassport(passport)) {
			validPassportCount++
			if (isStrictlyValidPassport(passport))
				strictlyValidPassportCount++
		}
		passport = {}
		continue
	}
	
	addFieldsToPassport(passport, line)
}

console.log(validPassportCount)
console.log(strictlyValidPassportCount)
