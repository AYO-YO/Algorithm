package cn.ayo.jsk;

import java.util.Scanner;

// https://nanti.jisuanke.com/t/T1201
public class T1201 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int a = scan.nextInt(), b = scan.nextInt(), c = scan.nextInt();
        int r = 2;
        while (true) {
            if (a % r == b % r && a % r == c % r) {
                System.out.println(r);
                return;
            }
            r++;
        }
    }
}