const util = require('./util.js');

function solvePart1(instructions) {
	let x = 0
	let y = 0
	let r = 360000

	for (let inst of instructions) {
		if (inst.action == 'N')
			y += inst.value
		if (inst.action == 'E')
			x += inst.value
		if (inst.action == 'S')
			y -= inst.value
		if (inst.action == 'W')
			x -= inst.value
		if (inst.action == 'R')
			r += inst.value
		if (inst.action == 'L')
			r -= inst.value
		if (inst.action == 'F') {
			let dir = (r % 360) / 90
			if (dir == 0)
				x += inst.value
			else if (dir == 1)
				y -= inst.value
			else if (dir == 2)
				x -= inst.value
			else if (dir == 3)
				y += inst.value
		}
	}

	return Math.abs(x) + Math.abs(y)
}

const rotate = ([dx, dy], degrees) => ({
	0:   [ dx,  dy],
	90:  [-dy,  dx],
	180: [-dx, -dy],
	270: [ dy, -dx],
}[(degrees + 360) % 360]);

function solvePart2(instructions) {
	let x = 0
	let y = 0
	let waypointx = 10
	let waypointy = 1

	for (let inst of instructions) {
		if (inst.action == 'N')
			waypointy += inst.value
		if (inst.action == 'E')
			waypointx += inst.value
		if (inst.action == 'S')
			waypointy -= inst.value
		if (inst.action == 'W')
			waypointx -= inst.value
		if (inst.action == 'R') {
			[waypointx, waypointy] = rotate([waypointx, waypointy], -inst.value)
		}
		if (inst.action == 'L') {
			[waypointx, waypointy] = rotate([waypointx, waypointy], inst.value)
		}
		if (inst.action == 'F') {
			x += inst.value * waypointx
			y += inst.value * waypointy
		}
	}

	return Math.abs(x) + Math.abs(y)
}

(function() {
	let input = util.readLines('input/day12.txt')

	let instructions = []
	for (let line of input) {
		instructions.push({
			action: line.charAt(0),
			value: parseInt(line.substring(1))
		})
	}

	console.log(solvePart1(instructions)) // 508
	console.log(solvePart2(instructions)) // 30761
}())
