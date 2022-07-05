package factorial

import "testing"

func TestFactorial(t *testing.T) {
	factorial := Factorial(1)

	if factorial != 1 {
		t.Fatalf("Factorial did not returned as expected, expected %d, received %d", 1, factorial)
	}

	factorial = Factorial(2)

	if factorial != 2 {
		t.Fatalf("Factorial did not returned as expected, expected %d, received %d", 2, factorial)
	}

	factorial = Factorial(10)

	if factorial != 3628800 {
		t.Fatalf("Factorial did not returned as expected, expected %d, received %d", 3628800, factorial)
	}

	factorial = Factorial(14)

	if factorial != 87178291200 {
		t.Fatalf("Factorial did not returned as expected, expected %d, received %d", 87178291200, factorial)
	}

	factorial = Factorial(0)

	if factorial != 1 {
		t.Fatalf("Factorial did not returned as expected, expected %d, received %d", 1, factorial)
	}
}
