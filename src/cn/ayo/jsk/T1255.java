package cn.ayo.jsk;

import java.util.Scanner;

// https://nanti.jisuanke.com/t/T1255
public class T1255 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int m = sc.nextInt();
        int n = sc.nextInt();
        StringBuilder sb = new StringBuilder();
        for (int i = m; i <= n; i++) {
            if (isArmstrong(i))
                sb.append(i).append(" ");
        }
        System.out.println(sb.length() > 0 ? sb : "none");
    }

    private static boolean isArmstrong(int n) {
        char[] str = String.valueOf(n).toCharArray();
        int l = str.length;
        int s = 0;
        for (char c : str) {
            s += Math.pow(c - 48, l);
        }
        return s == n;
    }
}
