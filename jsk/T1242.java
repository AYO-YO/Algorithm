package cn.ayo.jsk;

import java.util.Scanner;

/**
 * https://nanti.jisuanke.com/t/T1242
 * 本题的思路主要为质因数分解，若要产生一个0，则至少需要一个2*5
 * 质因数分解2肯定比5多，所以变相的即为求质因式分解中5的个数
 * 若能被5整除，则至少有一个5，若其除数还能被5整除，则5中有5
 * 例如：25=5*5；50=2*5*5；100=2*2*5*5；125=5*5*5；
 */
public class T1242 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int m = sc.nextInt();
        int n = sc.nextInt();
        int c = 0;
        for (int j = m; j <= n; j++) {
            int t = j;
            while (t % 5 == 0) {
                c++;
                t /= 5;
            }
        }
        System.out.println(c);
    }
}
