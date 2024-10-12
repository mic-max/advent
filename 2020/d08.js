const util = require('../util.js');

(function() {
	let input = util.readLines('input.txt')

	let rules = []
	for (let line of input) {
		rules.push({
			op: line.substring(0, 3),
			arg: parseInt(line.replace('+', '').substring(4))
		})
	}

	let accumulator = 0
	let curInstruction = 0

	let ops = {
		nop: (x) => {
			curInstruction++
		},
		acc: (x) => {
			accumulator += x
			curInstruction++
		},
		jmp: (x) => {
			curInstruction += x
		}
	}

	let runLines = new Set()
	while (curInstruction < rules.length) {
		if (runLines.has(curInstruction))
			break
		runLines.add(curInstruction)
		ops[rules[curInstruction].op](rules[curInstruction].arg)
	}

	console.log(accumulator) // 1818

	outer:
	for (let i = 0; i < rules.length; i++) {
		curInstruction = 0
		accumulator = 0
		if (rules[i].op === 'jmp')
			rules[i].op = 'nop'
		else if (rules[i].op === 'nop')
			rules[i].op = 'jmp'
		else
			continue

		let runLinesCopy = new Set()
		while (curInstruction < rules.length) {
			if (runLinesCopy.has(curInstruction)) {
				if (rules[i].op === 'jmp')
					rules[i].op = 'nop'
				else if (rules[i].op === 'nop')
					rules[i].op = 'jmp'
				continue outer
			}
			runLinesCopy.add(curInstruction)
			ops[rules[curInstruction].op](rules[curInstruction].arg)
		}
		break
	}

	console.log(accumulator) // 631
}())
