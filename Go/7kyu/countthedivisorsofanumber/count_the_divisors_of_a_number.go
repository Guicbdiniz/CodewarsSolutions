package countthedivisorsofanumber

func Divisors(n int) int {
	divisorsSum := 0

	for i := 1; i <= n; i++ {
		if n%i == 0 {
			divisorsSum++
		}
	}

	return divisorsSum
}
