const util = require('./util.js')

let computeSeatId = (row, column) => row * 8 + column

function getRow(value) {
	return parseInt(value.replace(/F/g, '0').replace(/B/g, '1'), 2)
}

function getColumn(value) {
	return parseInt(value.replace(/L/g, '0').replace(/R/g, '1'), 2)
}

function findMySeat(seatIds) {
	seatIds.sort()

	for (let i = 0; i < seatIds.length; i++) {
		if (seatIds[i + 1] - seatIds[i] == 2)
			return seatIds[i] + 1
	}

	return -1
}

let input = util.readLines('input/day05.txt')

let seatIds = []

for (let line of input) {
	let row = getRow(line.substring(0, 7))
	let column = getColumn(line.substring(7))
	let seatId = computeSeatId(row, column)
	seatIds.push(seatId)
}

let highestSeatId = Math.max(...seatIds)
let mySeat = findMySeat(seatIds)

console.log(highestSeatId)
console.log(mySeat)
