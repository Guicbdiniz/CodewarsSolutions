/**  
 * Highest Rank Number in an Array 6kyu
 * https://www.codewars.com/kata/5420fc9bb5b2c7fd57000004
 * 
 * Complete the method which returns the number which is most frequent in the given input array. 
 * If there is a tie for most frequent number, return the largest number among them.
*/

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
