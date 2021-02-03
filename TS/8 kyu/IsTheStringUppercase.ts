/* Is the string uppercase? - 8kyu
 * https://www.codewars.com/kata/56cd44e1aa4ac7879200010b
 *
 * Create a method is_upcase? to see whether the string is ALL CAPS.
 *
 * In this Kata, a string is said to be in ALL CAPS whenever it does not contain any lowercase letter
 * so any string containing no letters at all is trivially considered to be in ALL CAPS.
 */

export function isUpperCase(str: string) {
  return str.toUpperCase() === str;
}
