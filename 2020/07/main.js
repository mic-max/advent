const util = require('../util.js');

function findContainingBagColours(allBags, colour) {
	let answer = []
	for (let i in allBags) {
		if (allBags[i].hasOwnProperty(colour))
			answer.push(i)
	}
	return answer
}

function getElementFromSet(set) {
	for (const entry of set)
		return entry
}

function bagInThisOne(allBags, colour) {
	if (util.isEmpty(allBags[colour]))
		return 1

	let sum = 1
	for (let inside in allBags[colour])
		sum += allBags[colour][inside] * bagInThisOne(allBags, inside)
	return sum
}

(function() {
	let input = util.readLines('input.txt')

	let allBags = {}
	for (let line of input) {
		let match = /^(.+) bags contain (.+).$/.exec(line)
		let contains = {}
		if (match[2] !== 'no other bags') {
			for (let innerBag of match[2].split(', ')) {
				let innerMatch = /^(\d+) (.+) bags?$/.exec(innerBag)
				contains[innerMatch[2]] = parseInt(innerMatch[1])
			}
		}
		allBags[match[1]] = contains
	}

	let containingBags = new Set(['shiny gold'])
	let answerBags = new Set()
	while (containingBags.size > 0) {
		let bag = getElementFromSet(containingBags)
		let c = findContainingBagColours(allBags, bag)
		for (let conBag of c)
			containingBags.add(conBag)
		answerBags.add(bag)
		containingBags.delete(bag)
	}

	console.log(answerBags.size - 1) // 139
	console.log(bagInThisOne(allBags, 'shiny gold') - 1) // 58175
}())
