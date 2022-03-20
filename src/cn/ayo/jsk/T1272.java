package cn.ayo.jsk;

import java.util.Scanner;

// https://nanti.jisuanke.com/t/T1272
public class T1272 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = n ^ (n - 1);
        int c = 0;
        char[] bin = Integer.toBinaryString(m).toCharArray();
        for (char ch : bin)
            if (ch == '1')
                c++;
        System.out.println(c);
    }
}
