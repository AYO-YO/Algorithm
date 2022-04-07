package cn.ayo.jsk;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

// https://nanti.jisuanke.com/t/T1199
public class T1199 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String inp = br.readLine();
        int n = Integer.parseInt(inp.split(" ")[0]);
        int k = Integer.parseInt(inp.split(" ")[1]);
        String[] lists = br.readLine().split(" ");
        int[] nums = new int[lists.length];
        for (int i = 0; i < lists.length; i++) {
            nums[i] = Integer.parseInt(lists[i]);
        }
        for (int i = 0; i <= nums.length / 2; i++) {
            int tmp = k - nums[i];
            if (listHas(nums, tmp)) {
                System.out.println("yes");
                return;
            }
        }
        System.out.println("no");
    }

    private static boolean listHas(int[] nums, int tmp) {
        for (int i : nums)
            if (tmp == i) return true;
        return false;
    }
}
