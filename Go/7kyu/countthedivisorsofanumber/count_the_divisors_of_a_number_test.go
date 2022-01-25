package countthedivisorsofanumber

import "testing"

func TestDivisorsFromOne(t *testing.T) {
	divisors := Divisors(1)
	if divisors != 1 {
		t.Errorf("Divisors of 1 did not return the correct value, got %d, expected %d", divisors, 1)
	}
}

func TestDivisorsFromTen(t *testing.T) {
	divisors := Divisors(10)
	if divisors != 4 {
		t.Errorf("Divisors of 10 did not return the correct value, got %d, expected %d", divisors, 4)
	}
}
