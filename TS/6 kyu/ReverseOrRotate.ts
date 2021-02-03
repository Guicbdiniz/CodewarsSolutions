/*
 * Reverse or rotate? - 6kyu
 * https://www.codewars.com/kata/56b5afb4ed1f6d5fb0000991
 *
 * Access the link for a long task description.
 */

export class G964 {
  public static revrot(str: string, sz: number) {
    if (str === "" || sz <= 0 || sz > str.length) {
      return "";
    } else {
      let finalString = "";

      let strBeggining = 0;
      for (let i = sz; i <= str.length; i += sz) {
        const current = str.substring(strBeggining, i);

        const sumOfCubesIsEven =
          current
            .split("")
            .map((letter) => parseInt(letter) ** 3)
            .reduce((x, y) => x + y, 0) %
            2 ==
          0;

        if (sumOfCubesIsEven) {
          finalString += current.split("").reverse().join("");
        } else {
          const firstDigit = current.charAt(0);
          for (let j = 1; j < current.length; j++) {
            finalString += current.charAt(j);
          }
          finalString += firstDigit;
        }
        strBeggining += sz;
      }
      return finalString;
    }
  }
}
