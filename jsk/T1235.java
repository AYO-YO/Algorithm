package cn.ayo.jsk;

import java.util.Scanner;

public class T1235 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt(), b = sc.nextInt(), c = sc.nextInt();
        for (int i = 0; i < c; i++) {
            a %= b;
            a *= 10;
        }
        System.out.println(a / b);
    }
}
