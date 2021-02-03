/*
 * Even of Odd - 8kyu
 * https://www.codewars.com/kata/53da3dbb4a5168369a0000fe
 *
 * Create a function (or write a script in Shell) that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.
 */

export function even_or_odd(n: number): String {
  return n % 2 == 0 ? "Even" : "Odd";
}
