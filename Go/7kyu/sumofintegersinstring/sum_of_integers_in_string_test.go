package sumofintegersinstring

import "testing"

func TestWithZeroIntegers(t *testing.T) {
	sum := SumOfIntegersInString("no numbers here")

	if sum != 0 {
		t.Errorf("Sum of integers inside a string with no numbers did not return as expected, got %d, expected %d", sum, 0)
	}
}

func TestWithEmptyString(t *testing.T) {
	sum := SumOfIntegersInString("")

	if sum != 0 {
		t.Errorf("Sum of integers inside an empty string did not return as expected, got %d, expected %d", sum, 0)
	}
}

func TestWithSmallString(t *testing.T) {
	sum := SumOfIntegersInString("oi8leozinho9")

	if sum != 17 {
		t.Errorf("Sum of integers inside a small string did not return as expected, got %d, expected %d", sum, 17)
	}
}
