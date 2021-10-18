package partsofalist

import (
	"fmt"
	"strings"
)

func PartList(arr []string) string {
	result := ""
	for i := 0; i < len(arr)-1; i++ {
		arrCopy := make([]string, len(arr))
		copy(arrCopy, arr)
		arrCopy[i] = arrCopy[i] + ","
		result += fmt.Sprintf("(%s)", strings.Join(arrCopy, " "))
	}
	return result
}
