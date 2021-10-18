package maximumlengthdifference

import "testing"

func TestMxDifLgEmptyArrays(t *testing.T) {
	maxLengthDif := MxDifLg([]string{}, []string{})
	if maxLengthDif != -1 {
		t.Errorf("MxDigLg did not return the correct value, got: %d, expected: %d", maxLengthDif, -1)
	}
}

func TestMxDifLgSmallArrays(t *testing.T) {
	maxLengthDif := MxDifLg([]string{"a", "ab", "abc"}, []string{"a", "ab", "abc"})
	if maxLengthDif != 2 {
		t.Errorf("MxDigLg did not return the correct value, got: %d, expected: %d", maxLengthDif, 2)
	}
}

func TestMxDifLgMediumArrays(t *testing.T) {
	a1 := []string{"hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"}
	a2 := []string{"cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"}
	maxLengthDif := MxDifLg(a1, a2)
	if maxLengthDif != 13 {
		t.Errorf("MxDigLg did not return the correct value, got: %d, expected: %d", maxLengthDif, 13)
	}
}
