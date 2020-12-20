const util = require('../util.js');

function numAdjacent(seats, x, y) {
	let sum = 0
	for (let i = x - 1; i <= x + 1; i++) {
		for (let j = y - 1; j <= y + 1; j++) {
			if (i < 0 || i >= seats.length || j < 0 || j >= seats[0].length || i == x && j == y)
				continue
			if (seats[i][j] === '#')
				sum++
		}
	}
	return sum
}

function occupiedSeatsVisible(seats, x, y) {
	let sum = 0
	for (let i = x - 1; i <= x + 1; i++) {
		for (let j = y - 1; j <= y + 1; j++) {
			if (i == x && j == y)
				continue
			let xx = i
			let yy = j
			while (xx >= 0 && xx < seats.length && yy >= 0 && yy < seats[0].length && seats[xx][yy] === '.') {
				xx += i - x
				yy += j - y
			}
			if (xx >= 0 && xx < seats.length && yy >= 0 && yy < seats[0].length)
				sum += seats[xx][yy] === '#' ? 1 : 0
		}
	}
	return sum
}

// They are the same size
function areArraysEqual(arr1, arr2) {
	for (let i = 0; i < arr1.length; i++) {
		for (let j = 0; j < arr1[i].length; j++) {
			if (arr1[i][j] !== arr2[i][j])
				return false
		}
	}
	return true
}

function countOccupiedSeats(seats) {
	let sum = 0
	for (let i = 0; i < seats.length; i++) {
		for (let j = 0; j < seats[i].length; j++) {
			if (seats[i][j] === '#')
				sum++;
		}
	}
	return sum
}

function cloneArray(arr) {
	let clone = []
	for (var i = 0; i < arr.length; i++)
		clone[i] = arr[i].slice();
	return clone
}

// MAIN
let input = util.readLines('input.txt')

let seats = []
for (let line of input)
	seats.push(line.split(''))

let arraysAreTheSame = false
let newSeats = []
while (!arraysAreTheSame) {
	newSeats = cloneArray(seats)

	for (let i = 0; i < seats.length; i++) {
		for (let j = 0; j < seats[i].length; j++) {
			if (seats[i][j] === 'L' && occupiedSeatsVisible(seats, i, j) == 0)
				newSeats[i][j] = '#'
			else if (seats[i][j] === '#' && occupiedSeatsVisible(seats, i, j) >= 5)
				newSeats[i][j] = 'L'
		}
	}

	arraysAreTheSame = areArraysEqual(seats, newSeats)
	seats = cloneArray(newSeats)
}

console.log(countOccupiedSeats(seats)) // 2211
console.log() // 1995
