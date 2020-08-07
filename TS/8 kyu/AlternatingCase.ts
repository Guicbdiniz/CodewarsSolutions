// altERnaTIng cAsE <=> ALTerNAtiNG CaSe - 8kyu

export function toAlternatingCase(s: string): string {
	return s
		.split('')
		.map((letter) =>
			letter.toLowerCase() === letter
				? letter.toUpperCase()
				: letter.toLowerCase()
		)
		.join('')
}
