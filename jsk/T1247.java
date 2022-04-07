package cn.ayo.jsk;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

// https://nanti.jisuanke.com/t/T1247
public class T1247 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        ArrayList<Integer> arrayList = new ArrayList<>();
        for (int i = 100; i < 1000; i++) {
            if (isWqpf(i) && isLgsxt(i)) arrayList.add(i);
        }
        System.out.println(arrayList.get(n - 1));
    }

    private static boolean isWqpf(int n) {
        return (Math.floor(Math.sqrt(n)) * Math.floor(Math.sqrt(n))) == n;
    }

    private static boolean isLgsxt(int n) {
        char[] tmp = String.valueOf(n).toCharArray();
        Set<Character> set = new HashSet<>();
        for (char c : tmp) {
            set.add(c);
        }
        return tmp.length != set.size();
    }
}
