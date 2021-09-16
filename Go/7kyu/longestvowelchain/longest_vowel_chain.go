package longestvowelchain

import (
	"strings"
)

func Solve(s string) int {
	vowels := "aeiou"
	longestChain := 0
	currentChainSize := 0
	for i := 0; i < len(s); i++ {
		if strings.ContainsAny(vowels, s[i:i+1]) {
			currentChainSize++
			if currentChainSize > longestChain {
				longestChain = currentChainSize
			}
		} else {
			currentChainSize = 0
		}
	}
	return longestChain
}
