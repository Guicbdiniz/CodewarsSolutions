export function solution(str: string): string {
	if (str != '') {
		let reversed = ''

		for (let i = str.length - 1; i >= 0; i--) {
			reversed += String(str.charAt(i))
		}
		return reversed
	}
	return ''
}

export function MuchBetter(str: string): string {
	return str.split('').reverse().join('')
}
