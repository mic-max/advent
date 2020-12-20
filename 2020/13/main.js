const util = require('../util.js');

(function() {
	let input = util.readLines('input.txt')

    let earliest = parseInt(input[0])
    let busIds = input[1]
        .split(',')
        .filter(x => x != 'x')
        .map(x => parseInt(x))

    let bestBus = 0
    let shortestWait = 99999
    for (let bus of busIds) {
        let diff = bus - (earliest % bus)
        if (diff < shortestWait) {
            shortestWait = diff
            bestBus = bus
        }
    }

    let buses = input[1]
        .split(',')
        .map((x, i) => [i, x])
        .filter(x => x[1] != 'x')
        .map(x => [x[0], parseInt(x[1])])

	console.log(bestBus * shortestWait) // 370
	console.log() // 
}())
