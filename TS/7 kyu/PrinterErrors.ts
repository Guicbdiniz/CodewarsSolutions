// Printers Erros - 7kyu

// export class G964 {
// 	public static printerError(s: string): string {
// 		return (
// 			(s.match(/[n-z]/g) == null ? 0 : s.match(/[n-z]/g)?.length) +
// 			'/' +
// 			s.length
// 		)
// 	}
// }

// ??????????????????????????????

export class G964 {
	public static printerError(s: string): string {
		let mistakes = 0
		for (let letter of s) {
			for (let letter2 of 'nopqrstuvwxyz') {
				if (letter === letter2) {
					mistakes++
				}
			}
		}

		return mistakes + '/' + s.length
	}
}
