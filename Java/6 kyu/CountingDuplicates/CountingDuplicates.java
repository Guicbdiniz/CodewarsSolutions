import java.util.HashMap;
import java.util.Map;


/*
 * Counting Duplicates 6kyu
 * https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1
 *
 * Write a function that will return the count of distinct case-insensitive 
 * alphabetic characters and numeric digits that occur more than once in the input string.
 * 
 * The input string can be assumed to contain only alphabets (both uppercase and lowercase) 
 * and numeric digits.
*/

public class CountingDuplicates {
  public static int duplicateCount(String text) {
    Map<Character, Integer> charToRepetitions = new HashMap<Character, Integer>();

    for(char character: text.toLowerCase().toCharArray()){
      Character characterAsObject = Character.valueOf(character);

      if(charToRepetitions.containsKey(characterAsObject)){
        int numberOfRepetitions = charToRepetitions.get(characterAsObject).intValue();

        charToRepetitions.put(characterAsObject, numberOfRepetitions + 1);
      } else {
        charToRepetitions.put(characterAsObject, 1);
      }
    }

    int numberOfDuplicates = (int) charToRepetitions.entrySet().stream().filter(entry -> entry.getValue() > 1).count();

    return numberOfDuplicates;
  }

  public static void main(String[] args) {
    System.out.println(duplicateCount(args[0]));
  }
}