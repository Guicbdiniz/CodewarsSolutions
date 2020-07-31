export class Kata {
	static highAndLow(numbers: string) {
		const arrayOfNumbers = numbers
			.split(' ')
			.map((str) => parseInt(str))
			.sort((a, b) => a - b)
		return `${arrayOfNumbers[arrayOfNumbers.length - 1]} ${arrayOfNumbers[0]}`
	}
}
