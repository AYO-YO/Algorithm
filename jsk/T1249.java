package cn.ayo.jsk;

import java.util.Scanner;

// https://nanti.jisuanke.com/t/T1249
public class T1249 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        char[] inp = sc.nextLine().toCharArray();
        int c = inp[0];
        for (int i = 1; i < inp.length; i++) {
            c ^= inp[i];
        }
        System.out.println(c == 0 ? "Yes" : "No");
    }
}
