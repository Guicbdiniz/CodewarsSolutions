import java.lang.Math;

/*
 * Tortoise racing 6kyu
 * https://www.codewars.com/kata/55e2adece53b4cdcb900006c
 * 
 * Access the link for a long task description.
*/

import java.lang.Math;

public class Tortoise {
    public static int[] race(int speedA, int speedB, int leadAOverB) {

        if (speedA >= speedB) {
            return null;
        }

        double timeToBCatchAInTotal = leadAOverB * 1.0 / (speedB - speedA);

        int hoursToBCatchA = (int) Math.floor(timeToBCatchAInTotal);

        double minutesToBCatchATotal = (timeToBCatchAInTotal - hoursToBCatchA) * 60;

        int minutesToBCatchA = (int) Math.floor(minutesToBCatchATotal);

        double secondsToBCatchATotal = (minutesToBCatchATotal - minutesToBCatchA) * 60;

        int secondsToBCatchA = (int) Math.floor(secondsToBCatchATotal);

        return new int[] { hoursToBCatchA, minutesToBCatchA, secondsToBCatchA };
    }

}
