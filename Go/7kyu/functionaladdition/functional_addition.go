package functionaladdition

func Add(i int) func(int) int {
	return func(j int) int { return i + j }
}
