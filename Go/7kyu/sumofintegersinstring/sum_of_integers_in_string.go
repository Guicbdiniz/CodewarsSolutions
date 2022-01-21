package sumofintegersinstring

import (
	"strconv"
	"unicode"
)

func SumOfIntegersInString(strng string) int {
	sum := 0

	currentNumber := ""

	for _, v := range strng {
		if unicode.IsDigit(v) {
			numberAsString := string(v)
			currentNumber += numberAsString
		} else {
			if len(currentNumber) > 0 {
				numberToSum, _ := strconv.Atoi(currentNumber)
				sum += numberToSum
				currentNumber = ""
			}
		}
	}

	if len(currentNumber) > 0 {
		numberToSum, _ := strconv.Atoi(currentNumber)
		sum += numberToSum
	}

	return sum
}
