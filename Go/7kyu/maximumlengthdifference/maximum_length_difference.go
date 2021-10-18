package maximumlengthdifference

func MxDifLg(a1 []string, a2 []string) int {

	if len(a1) == 0 || len(a2) == 0 {
		return -1
	}

	maxA1, minA1 := getMaxAndMinLength(a1)
	maxA2, minA2 := getMaxAndMinLength(a2)

	if maxA1-minA2 > maxA2-minA1 {
		return maxA1 - minA2
	}
	return maxA2 - minA1
}

func getMaxAndMinLength(a []string) (int, int) {
	var max, min int
	for i, str := range a {
		if i == 0 {
			max = len(str)
			min = len(str)
		} else if max < len(str) {
			max = len(str)
		} else if min > len(str) {
			min = len(str)
		}
	}
	return max, min
}
