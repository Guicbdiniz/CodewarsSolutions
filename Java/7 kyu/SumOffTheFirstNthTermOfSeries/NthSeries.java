import java.text.DecimalFormat;
import java.text.DecimalFormatSymbols;
import java.util.Locale;

/*
 * Sum of the first nth term of Series
 * https://www.codewars.com/kata/555eded1ad94b00403000071/
 * 
 * Your task is to write a function which returns the sum of following series upto nth term(parameter).
 * 
 * Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...
*/

public class NthSeries {
    public static String seriesSum(int n) {

        float result = 0.0f;
        int denominator = 1;

        for (int i = 1; i <= n; i += 1) {
            result += (float) 1 / denominator;
            denominator += 3;
        }

        DecimalFormat decimalFormat = new DecimalFormat("0.00", DecimalFormatSymbols.getInstance(Locale.US));

        return decimalFormat.format(result);
    }

    public static void main(String[] args) {
        System.out.println(NthSeries.seriesSum(Integer.parseInt(args[0])));
    }
}
