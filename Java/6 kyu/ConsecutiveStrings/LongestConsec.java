import java.util.Arrays;

/*
 * Consecutive Strings 6kyu
 * https://www.codewars.com/kata/56a5d994ac971f1ac500003e
 * 
 * You are given an array(list) strarr of strings and an integer k. 
 * Your task is to return the first longest string consisting of k consecutive strings taken in the array.
 * 
 * n being the length of the string array, if n = 0 or k > n or k <= 0 return "".
*/

public class LongestConsec {

    public static String longestConsec(String[] strarr, int k) {

        if (k <= 0) {
            return "";
        }

        int arraySize = strarr.length;
        String longestSum = "";

        for (int initialIndex = 0; initialIndex + k - 1 < arraySize; initialIndex++) {
            String[] currentSubArray = Arrays.copyOfRange(strarr, initialIndex, initialIndex + k);
            String currentStrSum = Arrays.stream(currentSubArray).reduce("", String::concat);

            if (longestSum.length() < currentStrSum.length()) {
                longestSum = currentStrSum;
            }
        }

        return longestSum;
    }

    public static void main(String[] args) {

    }
}
