package howgreenismyvalley

import "sort"

func getSortedInput(input []int) []int {
	sorted := make([]int, len(input))
	copy(sorted, input)
	sort.Ints(sorted)
	return sorted
}

func MakeValley(input []int) []int {
	sortedInput := getSortedInput(input)
	output := make([]int, len(input))

	nextRightIndex := 0
	nextLeftIndex := len(sortedInput) - 1
	nextTurn := 0

	for i := len(sortedInput) - 1; i >= 0; i-- {
		if nextTurn == 0 {
			output[nextRightIndex] = sortedInput[i]
			nextRightIndex++
			nextTurn = 1
		} else {
			output[nextLeftIndex] = sortedInput[i]
			nextLeftIndex--
			nextTurn = 0
		}
	}

	return output
}
