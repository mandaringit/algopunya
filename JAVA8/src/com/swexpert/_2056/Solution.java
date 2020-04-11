package com.swexpert._2056;

import java.util.Scanner;
import java.io.FileInputStream;
import java.util.stream.IntStream;

class Solution {
    public static void main(String args[]) throws Exception {
        System.setIn(new FileInputStream("src/com/swexpert/_2056/input.txt"));
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();

        for (int test_case = 1; test_case <= T; test_case++) {
            String numbers = sc.next();

            String month_str = numbers.substring(4, 6);
            String day_str = numbers.substring(6);

            int month = Integer.parseInt(month_str);
            int day = Integer.parseInt(day_str);

            int[] day31 = new int[]{1, 3, 5, 7, 8, 10, 12};
            int[] day30 = new int[]{4, 6, 9, 11};

            boolean isValid = true;

            if (month == 2) {
                if (day < 1 || day > 28) isValid = false;
            } else if (IntStream.of(day31).anyMatch(x -> x == month)) {
                if (day < 1 || day > 31) isValid = false;
            } else if (IntStream.of(day30).anyMatch(x -> x == month)) {
                if (day < 1 || day > 30) isValid = false;
            } else {
                isValid = false;
            }
            System.out.printf("#%d %s\n", test_case, isValid ? year_str + "/" + month_str + "/" + day_str : -1);
        }
    }
}