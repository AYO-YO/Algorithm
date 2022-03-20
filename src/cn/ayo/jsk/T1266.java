package cn.ayo.jsk;

import java.util.Scanner;

// https://nanti.jisuanke.com/t/T1266
public class T1266 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine();
        for (int i = 0; i < n; i++) {
            String str = sc.nextLine();
            System.out.println(isTrue(str) ? "YES" : "NO");
        }
    }

    private static boolean isTrue(String str) {
        int a = 0;
        int l = 0;
        char[] tmp = str.toCharArray();
        for (char c : tmp) {
            switch (c) {
                case 'A' -> {
                    l = 0;
                    a++;
                    if (a > 1) return false;
                }
                case 'L' -> {
                    l++;
                    if (l >= 3) return false;
                }
                default -> l = 0;
            }
        }
        return true;
    }
}
