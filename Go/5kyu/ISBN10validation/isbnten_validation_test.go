package ISBN10validation

import "testing"

func TestIsValidISBN10(t *testing.T) {
	expected := true
	identifier := "1112223339"
	got := ValidISBN10(identifier)

	if expected != got {
		t.Fatalf("Should have returned true for 1112223339")
	}

	expected = true
	identifier = "048665088X"
	got = ValidISBN10(identifier)

	if expected != got {
		t.Fatalf("Should have returned true for 048665088X")
	}

	expected = false
	identifier = "1234512345"
	got = ValidISBN10(identifier)

	if expected != got {
		t.Fatalf("Should have returned false for 1234512345")
	}

	expected = false
	identifier = "1293"
	got = ValidISBN10(identifier)

	if expected != got {
		t.Fatalf("Should have returned false for 1293")
	}

	expected = false
	identifier = "ABCDEFGHIJ"
	got = ValidISBN10(identifier)

	if expected != got {
		t.Fatalf("Should have returned false for ABCDEFGHIJ")
	}
}

func TestIsDigit(t *testing.T) {
	expected := true
	value := byte('0')
	got := isDigit(value)

	if expected != got {
		t.Fatalf("Should have returned true for '0'")
	}

	expected = false
	value = byte('m')
	got = isDigit(value)

	if expected != got {
		t.Fatalf("Should have returned false for 'm'")
	}

	expected = false
	value = '('
	got = isDigit(value)

	if expected != got {
		t.Fatalf("Should have returned false for '('")
	}

	expected = true
	value = '9'
	got = isDigit(value)

	if expected != got {
		t.Fatalf("Should have returned true for '9'")
	}
}

func TestConvertByteToDigit(t *testing.T) {
	expected := 0
	value := "0"[0]
	got := convertByteToDigit(value)

	if expected != got {
		t.Fatalf("Should have returned 0 for '0', but got: %d", got)
	}

	expected = 9
	value = "9"[0]
	got = convertByteToDigit(value)

	if expected != got {
		t.Fatalf("Should have returned 9 for '9', but got: %d", got)
	}
}
