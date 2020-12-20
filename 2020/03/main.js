const util = require('../util.js')

function treesEncountered(input, right, down) {
	let trees = 0
	let positionX = right
	let positionY = down
	const lineLength = input[0].length

	while (positionY < input.length) {
		trees += input[positionY][positionX % lineLength] === '#' ? 1 : 0
		positionX += right
		positionY += down
	}

	return trees
}

(function() {
	let input = util.readLines('input.txt')

	let paths = [
		{right: 3, down: 1},
		{right: 1, down: 1},
		{right: 5, down: 1},
		{right: 7, down: 1},
		{right: 1, down: 2}
	]

	let encounters = paths.map(x => treesEncountered(input, x.right, x.down))
	let product = encounters.reduce((a, b) => a * b)

	console.log(encounters[0]) // 167
	console.log(product) // 736527114
}())
