package cn.ayo.jsk;

import java.util.Scanner;

// https://nanti.jisuanke.com/t/T1267
public class T1267 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine();
        for (int i = 0; i < n; i++) {
            char[] tmp = sc.nextLine().toCharArray();
            StringBuilder sb = new StringBuilder();
            for (int j = 0; j < tmp.length; j++) {
                if ('A' <= tmp[j] && tmp[j] <= 'Z') {
                    sb.append("_");
                    sb.append((char) (tmp[j] + 32));
                    continue;
                }
                if (tmp[j] == '_') {
                    j++;
                    sb.append((char) (tmp[j] - 32));
                    continue;
                }
                sb.append(tmp[j]);
            }
            System.out.println(sb);
        }
    }
}
