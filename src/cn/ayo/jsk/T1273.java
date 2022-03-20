package cn.ayo.jsk;

import java.util.Scanner;

// https://nanti.jisuanke.com/t/T1273
public class T1273 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (sc.hasNext()) {
            boolean hasHW = false;
            String str = sc.nextLine();
            for (int i = 0; i < str.length() - 1; i++) {
                if (str.charAt(i) == str.charAt(i + 1)) {
                    hasHW = true;
                    break;
                }
            }
            System.out.println(hasHW ? "YES" : "NO");
        }
    }
}
