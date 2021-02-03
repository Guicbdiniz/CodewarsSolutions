/*
 * Highest and Lowest
 * https://www.codewars.com/kata/554b4ac871d6813a03000035
 *
 * In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.
 */

export class Kata {
  static highAndLow(numbers: string) {
    const arrayOfNumbers = numbers
      .split(" ")
      .map((str) => parseInt(str))
      .sort((a, b) => a - b);
    return `${arrayOfNumbers[arrayOfNumbers.length - 1]} ${arrayOfNumbers[0]}`;
  }
}
