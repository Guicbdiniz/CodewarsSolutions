package factorial

func Factorial(n int) int {
	calculatedValues := make([]int, n+2)
	calculatedValues[0] = 1
	calculatedValues[1] = 1
	return RecursiveFactorial(n, calculatedValues)
}

func RecursiveFactorial(n int, calculatedValues []int) int {
	if calculatedValues[n] != 0 {
		return calculatedValues[n]
	} else {
		calculatedValues[n] = n * RecursiveFactorial(n-1, calculatedValues)
		return calculatedValues[n]
	}
}
