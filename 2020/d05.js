const util = require('../util.js')

function computeSeatId(value) {
	return parseInt(value.replace(/[FL]/g, '0').replace(/[BR]/g, '1'), 2)
}

function findMySeat(seatIds) {
	for (let i = 0; i < seatIds.length; i++) {
		if (seatIds[i + 1] - seatIds[i] == 2)
			return seatIds[i] + 1
	}
}

(function() {
	let input = util.readLines('input.txt')

	let seatIds = input.map(computeSeatId)
	seatIds.sort()

	console.log(seatIds[seatIds.length - 1]) // 861
	console.log(findMySeat(seatIds)) // 633
}())
