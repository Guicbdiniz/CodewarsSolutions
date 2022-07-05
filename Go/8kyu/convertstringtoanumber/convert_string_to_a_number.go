package convertstringtoanumber

import "strconv"

func StringToNumber(str string) int {
	converted, err := strconv.Atoi(str)
	if err != nil {
		return 0
	}
	return converted
}
