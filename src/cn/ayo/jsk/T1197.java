package cn.ayo.jsk;

import java.util.Scanner;

// https://nanti.jisuanke.com/t/T1197
public class T1197 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int m = scan.nextInt();
        int n = scan.nextInt();
        int[] nums = new int[m];
        for (int i = 0; i < m; i++) {
            nums[i] = scan.nextInt();
        }
        for (int i = 0; i < m; i++) {
            if (count(nums, nums[i]) > 1) System.out.println(count(nums, nums[i]) - 1);
            else System.out.println("BeiJu");
        }
    }

    private static int count(int[] nums, int num) {
        int c = 0;
        for (int i : nums) {
            if (i == num) c += 1;
        }
        return c;
    }
}
