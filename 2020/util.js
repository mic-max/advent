const fs = require('fs')

exports.readLines = (filename) => {
	try {
		const data = fs.readFileSync(filename, 'UTF-8')
		return data.split(/\r?\n/)
	} catch (err) {
		console.error(err)
	}
}

exports.inRangeInclusive = (value, min, max) => {
	return min <= value && value <= max
}

exports.isEmpty = (obj) => {
	return Object.keys(obj).length === 0;
}
