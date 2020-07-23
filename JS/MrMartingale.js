// Mr Martingale 7kyu

function martingale(bank, outcomes) {
	currentStake = 100
	currentBank = bank

	for (outcome of outcomes) {
		if (outcome == 1) {
			currentBank += currentStake
			currentStake = 100
		} else {
			currentBank -= currentStake
			currentStake *= 2
		}
	}

	return currentBank
}

console.log(martingale(1000, [1, 1, 0, 0, 1, 1, 0]))
