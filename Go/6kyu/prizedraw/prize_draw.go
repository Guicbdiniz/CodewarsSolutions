package prizedraw

import "strings"

func NthRank(st string, we []int, n int) string {
	if len(st) == 0 {
		return "No participants"
	}

	fns := strings.Split(st, ",")

	if len(fns) < n {
		return "Not enough participants"
	}

	wn := make([]int, len(fns))
	for i, fn := range fns {
		wn[i] = getSom(fn) * we[i]
	}

	ordered := make([]string, len(fns))
	for i := 0; i < len(fns); i++ {
		greaterIndex := i
		for j := i + 1; j < len(fns); j++ {
			if wn[j] > wn[greaterIndex] {
				greaterIndex = j
			} else if wn[j] == wn[greaterIndex] {
				c := strings.Compare(fns[j], fns[greaterIndex])
				if c == 1 {
					greaterIndex = j
				}
			}
		}
		ordered[i] = fns[greaterIndex]
	}
	return ordered[n-1]
}

func getSom(st string) int {
	som := len(st)

	for _, l := range st {
		som += getRank(l)
	}

	return som
}

func getRank(r rune) int {
	if r > 'Z' {
		return int(r) - 'a' + 1
	}
	return int(r) - 'A' + 1
}
