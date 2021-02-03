/*
 * Reversed Strings 8kyu
 * https://www.codewars.com/kata/5168bb5dfe9a00b126000018
 *
 * Complete the solution so that it reverses the string passed into it.
 */

export function solution(str: string): string {
  if (str != "") {
    let reversed = "";

    for (let i = str.length - 1; i >= 0; i--) {
      reversed += String(str.charAt(i));
    }
    return reversed;
  }
  return "";
}

export function MuchBetter(str: string): string {
  return str.split("").reverse().join("");
}
