package convertstringtoanumber

import "testing"

func TestStringToNumber(t *testing.T) {
	numberString := StringToNumber("15")
	if numberString != 15 {
		t.Errorf("StringToNumber did not returned as expected, expected %d, returned %d", 15, numberString)
	}
}
