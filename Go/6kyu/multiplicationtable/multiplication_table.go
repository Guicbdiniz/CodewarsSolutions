package multiplicationtable

// Create a MultiplicationTable with required size
func MultiplicationTable(size int) [][]int {
	if size == 0 {
		return nil
	}
	multiplicationTable := make([][]int, size)
	for i := 0; i < size; i++ {
		multiplicationTable[i] = make([]int, size)
	}

	for i := 0; i < size; i++ {
		multiplicationTable[0][i] = i + 1
		multiplicationTable[i][0] = i + 1
	}

	for i := 1; i < size; i++ {
		for j := 1; j < size; j++ {
			multiplicationTable[i][j] = multiplicationTable[0][i] * multiplicationTable[j][0]
		}
	}

	return multiplicationTable
}
