package cn.ayo.jsk;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.HashMap;
import java.util.Map;

// https://nanti.jisuanke.com/t/T1234
public class T1234 {
    public static void main(String[] args) throws IOException {
        Map<BigInteger, String> getEn = new HashMap<>();
        getEn.put(BigInteger.valueOf(0), "Sunday");
        getEn.put(BigInteger.valueOf(1), "Monday");
        getEn.put(BigInteger.valueOf(2), "Tuesday");
        getEn.put(BigInteger.valueOf(3), "Wednesday");
        getEn.put(BigInteger.valueOf(4), "Thursday");
        getEn.put(BigInteger.valueOf(5), "Friday");
        getEn.put(BigInteger.valueOf(6), "Saturday");
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] tmp = br.readLine().split(" ");
        BigInteger a = new BigInteger(tmp[0]);
        int b = Integer.parseInt(tmp[1]);
        a = a.pow(b);
        a = a.divideAndRemainder(BigInteger.valueOf(7))[1];
        System.out.println(getEn.get(a));
    }
}
