import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

/* 
 * Encrypt this! 6kyu
 * https://www.codewars.com/kata/5848565e273af816fb000449
 * 
 * Access the link for a long task description.
*/

public class Kata {
    public static String encryptThis(String text) {
        List<String> listOfWords = Arrays.asList(text.split(" "));
        // Arrays.stream(text.split(" ")) next time.

        return listOfWords.stream().map(Kata::encryptWord).collect(Collectors.joining(" "));
    }

    private static String encryptWord(String word) {
        String encryptedWord = "";

        // Not very proud of this.
        if (word.length() > 0) {
            encryptedWord += (int) word.charAt(0);
            if (word.length() > 1) {
                encryptedWord += word.charAt(word.length() - 1);
                if (word.length() > 2) {
                    encryptedWord += word.substring(2, word.length() - 1) + word.charAt(1);
                }
            }
        }

        return encryptedWord;
    }

    public static void main(String[] args) {
        System.out.println(encryptThis("A wise old owl lived in an oak"));
    }
}
