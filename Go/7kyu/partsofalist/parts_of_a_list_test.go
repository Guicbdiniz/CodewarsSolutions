package partsofalist

import "testing"

func TestPartListSmallArray(t *testing.T) {
	result := PartList([]string{"a", "b", "c", "d"})
	expected := "(a, b c d)(a b, c d)(a b c, d)"
	if result != expected {
		t.Errorf("PartList did not return the correct value, got: %s, expected: %s", result, expected)
	}
}
