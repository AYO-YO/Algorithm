package cn.ayo.jsk;

import java.math.BigInteger;
import java.util.Scanner;

// https://nanti.jisuanke.com/t/T1237
public class T1237 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int m = sc.nextInt();
        int n = sc.nextInt();
        BigInteger bm = BigInteger.valueOf(m);
        bm = bm.pow(n);
        System.out.printf("%03d", bm.remainder(BigInteger.valueOf(1000)));
    }
}
