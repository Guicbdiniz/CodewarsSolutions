/** 
 * Mr Martingale 7kyu  
 * https://www.codewars.com/kata/5eb34624fec7d10016de426e
 * 
 * You're in the casino, playing Roulette, going for the "1-18" bets only and desperate to beat the house 
 * and so you want to test how effective the Martingale strategy is.
 * 
 * You will be given a starting cash balance and an array of binary digits to represent a win (1) or a loss (0). Return your balance after playing all rounds.
 * 
 * You start with a stake of 100 dollars. If you lose a round, you lose the stake placed 
 * on that round and you double the stake for your next bet. When you win, you win 100% of the stake and revert back to staking 100 dollars on your next bet.
*/

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
