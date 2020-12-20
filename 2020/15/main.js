const util = require('../util.js');

(function() {
	let input = util.readLines('input.txt')

	let numbers = input[0]
		.split(',')
		.map(x => parseInt(x))
	let lastSaid = {}
	
	for (let i = 0; i < numbers.length - 1; i++)
		lastSaid[numbers[i]] = i + 1

	let lastSpoken = numbers[numbers.length - 1]
	let wasFirstSpoken = lastSaid[lastSpoken] || 0
	lastSaid[lastSpoken] = numbers.length

	for (let i = numbers.length + 1; i <= 10; i++) {
		console.log('index:', i)
		console.log(lastSaid)
		console.log(wasFirstSpoken)
		wasFirstSpoken = lastSaid[lastSpoken] || 0
		if (wasFirstSpoken == 0) {
			lastSpoken = 0
		} else {
			lastSpoken = i - lastSaid[lastSpoken]
		}
		lastSaid[lastSpoken] = i
		console.log(lastSpoken)
	}

	// console.log(lastSpoken) // 
	// console.log() // 
}())
