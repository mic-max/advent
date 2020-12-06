const util = require('./util.js')

let input = util.readLines('day03_input.txt')

function treesEncountered(input, right, down) {
	let positionX = right
	let positionY = down
	let trees = 0

	const lineLength = input[0].length
	while (positionY < input.length) {
		if (input[positionY][positionX % lineLength] === '#')
			trees++

		positionX += right
		positionY += down
	}

	return trees
}

let trees1 = treesEncountered(input, 3, 1)
let trees2 = treesEncountered(input, 1, 1)
let trees3 = treesEncountered(input, 5, 1)
let trees4 = treesEncountered(input, 7, 1)
let trees5 = treesEncountered(input, 1, 2)

let answer2 = trees1 * trees2 * trees3 * trees4 * trees5

console.log(trees1)
console.log(answer2)
