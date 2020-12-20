const util = require('../util.js');

function solvePartTwo(adapters) {
    adapters.unshift(0)
    adapters.push(adapters[adapters.length - 1] + 3)
    let pow2 = 0
    let pow7 = 0
    for (let i = 1; i < adapters.length - 1; i++)
    {
        let negative3 = (i >= 3) ? adapters[i - 3] : -9999
        if (adapters[i + 1] - negative3 == 4)
        {
            pow7 += 1
            pow2 -= 2
        }
        else if (adapters[i + 1] - adapters[i - 1] == 2)
        {
            pow2 += 1
        }
    }
    return Math.pow(2,pow2) * Math.pow(7, pow7)
}

(function() {
	let input = util.readLines('input.txt')
	let adapters = input.map(x => parseInt(x)).sort((a, b) => a - b)

	let lastJoltage = 0
	let diff1 = 0;
	let diff3 = 1;
	for (let joltage of adapters) {
		let diff = joltage - lastJoltage
		if (diff == 1) {
			diff1++
		} else if (diff == 3) {
			diff3++
		}
		lastJoltage = joltage
	}

	console.log(diff1 * diff3) // 2048
	console.log(solvePartTwo(adapters)) // 1322306994176
}())
