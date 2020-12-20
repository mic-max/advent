const util = require('../util.js');

function calcMaskValue(mask, value) {
	let binaryString = make36BitBinaryString(value)
	let result = ''
	for (let i = 0; i < mask.length; i++)
		result += mask[i] === 'X' ? binaryString[i] : mask[i]
	return parseInt(result, 2)
}

function countXs(str) {
	return str.split('').filter(x => x === 'X').length
}

function make36BitBinaryString(value) {
	return value.toString(2).padStart(36, '0')
}

function decodeAddy(mask, value) {
	let result = ''
	let maskIndex = 0
	for (let i = 0; i < value.length; i++)
		result += value[i] === 'X' ? mask[maskIndex++] : value[i]
	return parseInt(result, 2)
}

function memoryAddrDecoder(mask, addr) {
	let addys = []
	let binaryString = make36BitBinaryString(addr)
	let result = ''

	for (let i = 0; i < mask.length; i++)
		result += mask[i] === '0' ? binaryString[i] : mask[i] === '1' ? '1' : 'X'

	let numXs = countXs(result)
	for (let i = 0; i < Math.pow(2, numXs); i++) {
		let curMask = i.toString(2).padStart(numXs, '0')
		let decodedAddy = decodeAddy(curMask, result)
		addys.push(decodedAddy)
	}
	return addys
}

(function() {
	let input = util.readLines('input.txt')

	let mask = ''
	let mem = {}

	for (let line of input) {
		if (line.startsWith('mask')) {
			mask = line.substring(7)
		} else if (line.startsWith('mem')) {
			let addr = parseInt(line.substring(4, line.indexOf(']')))
			let value = parseInt(line.substring(line.indexOf('=') + 2))
			mem[addr] = calcMaskValue(mask, value)
		}
	}
	let sum1 = Object.values(mem).reduce((a, b) => a + b, 0)

	mask = ''
	mem = {}
	for (let line of input) {
		if (line.startsWith('mask')) {
			mask = line.substring(7)
		} else if (line.startsWith('mem')) {
			let addr = parseInt(line.substring(4, line.indexOf(']')))
			let value = parseInt(line.substring(line.indexOf('=') + 2))
			for (let addrDecoded of memoryAddrDecoder(mask, addr))
				mem[addrDecoded] = value
		}
	}

	let sum2 = Object.values(mem).reduce((a, b) => a + b, 0)

	console.log(sum1) // 6559449933360
	console.log(sum2) // 3369767240513
}())
