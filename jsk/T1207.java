package cn.ayo.jsk;

import java.util.Scanner;

// https://nanti.jisuanke.com/t/T1207
public class T1207 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int m = sc.nextInt();
        int[] nums = new int[m];
        int max = 0;
        for (int i = 0; i < m; i++) {
            nums[i] = sc.nextInt();
            if (nums[i] > max)
                max = nums[i];
        }
        int[] res = new int[max];
        res[0] = 1;
        res[1] = 2;
        for (int i = 2; i < max; i++) {
            res[i] = (2 * res[i - 1] + res[i - 2]) % 32767;
        }
        for (int i : nums) {
            System.out.println(res[i - 1]);
        }
    }
}
