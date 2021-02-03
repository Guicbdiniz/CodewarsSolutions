/*
 * altERnaTIng cAsE <=> ALTerNAtiNG CaSe - 8kyu
 * https://www.codewars.com/kata/56efc695740d30f963000557
 *
 * Define String.prototype.toAlternatingCase (or a similar function/method such as to_alternating_case/toAlternatingCase/ToAlternatingCase
 * in your selected language; see the initial solution for details) such that each lowercase letter becomes uppercase and each uppercase
 * letter becomes lowercase.
 */

export function toAlternatingCase(s: string): string {
  return s
    .split("")
    .map((letter) =>
      letter.toLowerCase() === letter
        ? letter.toUpperCase()
        : letter.toLowerCase()
    )
    .join("");
}
