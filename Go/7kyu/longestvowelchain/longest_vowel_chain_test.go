package longestvowelchain

import "testing"

func TestSolveWithEmptyString(t *testing.T) {
	longestVowelChain := Solve("")
	if longestVowelChain != 0 {
		t.Errorf(
			"Solve did not return the correct value, got: %d, expected: %d",
			longestVowelChain, 0,
		)
	}
}

func TestSolveWithSmallString(t *testing.T) {
	longestVowelChain := Solve("abcde")
	if longestVowelChain != 1 {
		t.Errorf(
			"Solve did not return the correct value, got: %d, expected: %d",
			longestVowelChain, 1,
		)
	}
}

func TestSolveWithMediumString(t *testing.T) {
	longestVowelChain := Solve("aapooilkyuipeeeolqpsetuioqmz")
	if longestVowelChain != 4 {
		t.Errorf(
			"Solve did not return the correct value, got: %d, expected: %d",
			longestVowelChain, 4,
		)
	}
}

func TestSolveWithLargeString(t *testing.T) {
	longestVowelChain := Solve("sapdoihaspeiujabwoeqabwejklqsnadqsndoqwbeqwjhebqwoeuqbwelqjwbeqweqbweqwjelhqwebqwoehqw")
	if longestVowelChain != 3 {
		t.Errorf(
			"Solve did not return the correct value, got: %d, expected: %d",
			longestVowelChain, 3,
		)
	}
}
