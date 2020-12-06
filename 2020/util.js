const fs = require('fs')

exports.readLines = function readLines(filename) {
	try {
		const data = fs.readFileSync(filename, 'UTF-8');
		return data.split(/\r?\n/);
	} catch (err) {
		console.error(err)
	}
}
