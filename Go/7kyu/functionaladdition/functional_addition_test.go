package functionaladdition

import "testing"

func TestAddWithZeroSum(t *testing.T) {
	addZero := Add(0)
	sum := addZero(0)
	if sum != 0 {
		t.Errorf("Function created to sum zero did not return the correct value with 0 param, got: %d, expected: %d",
			sum,
			0)
	}
	sum = addZero(5)
	if sum != 5 {
		t.Errorf("Function created to sum zero did not return the correct value with 5 param, got: %d, expected: %d",
			sum,
			5)
	}
}

func TestAddWithTenSum(t *testing.T) {
	addZero := Add(10)
	sum := addZero(0)
	if sum != 10 {
		t.Errorf("Function created to sum ten did not return the correct value with 0 param, got: %d, expected: %d",
			sum,
			10)
	}
	sum = addZero(5)
	if sum != 15 {
		t.Errorf("Function created to sum ten did not return the correct value with 5 param, got: %d, expected: %d",
			sum,
			15)
	}
}

func TestAddWithNegativeSum(t *testing.T) {
	addZero := Add(-5)
	sum := addZero(0)
	if sum != -5 {
		t.Errorf("Function created to sum minus five did not return the correct value with 0 param, got: %d, expected: %d",
			sum,
			-5)
	}
	sum = addZero(5)
	if sum != 0 {
		t.Errorf("Function created to sum minus 5 did not return the correct value with 5 param, got: %d, expected: %d",
			sum,
			0)
	}
}
