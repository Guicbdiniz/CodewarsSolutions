package multiplicationtable

import (
	"reflect"
	"testing"
)

func TestMultiplicationTableWithZeroValue(t *testing.T) {
	multiplicationTable := MultiplicationTable(0)
	if multiplicationTable != nil {
		t.Errorf(
			"MultiplicationTable function did not return nil after receiving size 0, got: %v, wanted: %v",
			multiplicationTable,
			nil,
		)
	}
}

func TestMultiplicationTableWithSmallSize(t *testing.T) {
	multiplicationTable := MultiplicationTable(1)
	if !reflect.DeepEqual(multiplicationTable, [][]int{{1}}) {
		t.Errorf(
			"MultiplicationTable function did not return a correct multiplication table, got: %v, wanted: %v",
			multiplicationTable,
			[][]int{{1}},
		)
	}
}

func TestMultiplicationTableWithMediumSize(t *testing.T) {
	multiplicationTable := MultiplicationTable(3)
	if !reflect.DeepEqual(multiplicationTable, [][]int{{1, 2, 3}, {2, 4, 6}, {3, 6, 9}}) {
		t.Errorf(
			"MultiplicationTable function did not return a correct multiplication table, got: %v, wanted: %v",
			multiplicationTable,
			[][]int{{1, 2, 3}, {2, 4, 6}, {3, 6, 9}},
		)
	}
}

func TestMultiplicationTableWithLargeSize(t *testing.T) {
	multiplicationTable := MultiplicationTable(6)
	preFilledTable := [][]int{{1, 2, 3, 4, 5, 6}, {2, 4, 6, 8, 10, 12}, {3, 6, 9, 12, 15, 18}, {4, 8, 12, 16, 20, 24}, {5, 10, 15, 20, 25, 30}, {6, 12, 18, 24, 30, 36}}
	if !reflect.DeepEqual(multiplicationTable, preFilledTable) {
		t.Errorf(
			"MultiplicationTable function did not return a correct multiplication table, got: %v, wanted: %v",
			multiplicationTable,
			preFilledTable,
		)
	}
}
