package ISBN10validation

func ValidISBN10(isbn string) bool {
	sum := 0
	digit := 0

	for i := 0; i < len(isbn)-1; i++ {
		if !isDigit(isbn[i]) {
			return false
		}
		digit = convertByteToDigit(isbn[i])
		sum = sum + digit*(i+1)
	}

	lastByte := isbn[len(isbn)-1]

	if isDigit(lastByte) {
		digit = convertByteToDigit(lastByte)
		sum = sum + digit*10
	} else if rune(lastByte) == 'X' || rune(lastByte) == 'x' {
		sum = sum + 10*10
	} else {
		return false
	}

	return sum%11 == 0
}

func isDigit(c byte) bool {
	return c > 47 && c < 58
}

func convertByteToDigit(c byte) int {
	return int(c) - 48
}
