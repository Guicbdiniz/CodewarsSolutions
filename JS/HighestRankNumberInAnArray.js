// Highest Rank Number in an Array 6kyu

function highestRank(arr) {
	let ranks = {}

	for (value of arr) {
		if (ranks[value]) {
			ranks[value]++
		} else {
			ranks[value] = 1
		}
	}

	let valueWithHighestRank = arr[0]
	for (key in ranks) {
		if (ranks[valueWithHighestRank] < ranks[key]) {
			valueWithHighestRank = Number.parseInt(key)
		} else if (ranks[valueWithHighestRank] == ranks[key]) {
			valueWithHighestRank =
				Number.parseInt(key) > valueWithHighestRank
					? Number.parseInt(key)
					: valueWithHighestRank
		}
	}

	return valueWithHighestRank
}

console.log(highestRank([1, 1, 5, 5]))
