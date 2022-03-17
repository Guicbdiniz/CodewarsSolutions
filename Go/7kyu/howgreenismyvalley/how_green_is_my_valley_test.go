package howgreenismyvalley

import (
	"reflect"
	"testing"
)

func TestMakeValleyWithSimpleInput(t *testing.T) {
	simpleInput := []int{79, 35, 54, 19, 35, 25}
	output := MakeValley(simpleInput)
	expectedOutput := []int{79, 35, 25, 19, 35, 54}
	if !reflect.DeepEqual(output, expectedOutput) {
		t.Errorf("MakeValley did not return the correct value for a simple input. Got: %v, expected: %v", output, expectedOutput)
	}
}
